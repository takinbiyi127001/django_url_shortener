from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView


import uuid
from .models import Shortener
from .forms import ShortenerForm


class HomePageView(View):
    """View to show the shortener form, new URL and validate form submission"""

    template_name = "shorteners/index.html"

    def get(self, request):
        context = {"shortened_form": ShortenerForm()}
        return render(request, self.template_name, context=context)

    def post(self, request):
        shortened_form = ShortenerForm(request.POST)
        context = {}
        if shortened_form.is_valid():
            #  Form fields passed validation
            uid = str(uuid.uuid4())[:6]
            shortened_form.cleaned_data["uuid"] = uid
            long_url = shortened_form.cleaned_data["url"]
            short_id = shortened_form.cleaned_data["uuid"]

            # populate data with shortened form
            shortener = Shortener(url=long_url, uuid=short_id)
            shortener.save()

            # check length of long url and strip
            if len(long_url) > 56:
                long_url = long_url[:56] + "..."

            short_url = request.build_absolute_uri("/") + short_id
            context["shortened_form"] = shortened_form
            context["long_url"] = long_url
            context["short_url"] = short_url
            return render(request, self.template_name, context=context)

        context["errors"] = shortened_form.errors

        return render(request, self.template_name, context=context)


class ShortenerListView(ListView):
    model = Shortener
    template_name = "shorteners/list.html"


def redirect_url(request, id):
    """Redirect to the long URL and increment the time used.
    Raise 404 page not found if link is broken"""

    details = get_object_or_404(Shortener, uuid=id)
    details.time_used += 1
    details.save()
    return redirect(details.url)

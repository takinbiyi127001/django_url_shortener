from django import forms

from .models import Shortener

"""Define Django form class"""


class ShortenerForm(forms.Form):
    """Create a form, URLInput uses URLValidator to validat that the given value us a valid URL."""

    url = forms.URLField(
        widget=forms.URLInput(
            attrs={"class": "form-url", "placeholder": "Enter URL to shorten"}
        ), required=True, label="", error_messages={"required": "Url field is required!"},
    )

    class Meta:
        model = Shortener
        fields = ("url",)

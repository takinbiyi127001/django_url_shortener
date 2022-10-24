from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("list", views.ShortenerListView.as_view(), name="shortened_url"),
    path("<str:id>", views.redirect_url, name="redirect"),
]

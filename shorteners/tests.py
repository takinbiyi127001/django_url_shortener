from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView, ShortenerListView
from .models import Shortener

# Create your tests here.


class HomePageTests(TestCase):
    def setUp(self):
        home_url = reverse("index")
        self.response = self.client.get(home_url)

    # Testing homepage
    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    # Testing templates
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "shorteners/index.html")

    # Testing HTML
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "URL Shortener")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hey! Why am I on this page.")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class ShortenerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.shortener = Shortener.objects.create(
            url="https://instances.vantage.sh/", uuid="abf67e"
        )

    def test_short_url(self):
        self.assertEqual(f"{self.shortener.url}", "https://instances.vantage.sh/")
        self.assertEqual(f"{self.shortener.uuid}", "abf67e")
        self.assertEqual(len(self.shortener.uuid), 6)

    def test_saved_url_redirects(self):
        shortener = Shortener.objects.get(uuid="abf67e")
        self.assertEqual(self.shortener.url, shortener.url)


class ShortenerListPageTests(TestCase):
    def setUp(self):
        shortener_url = reverse("shortened_url")
        self.response = self.client.get(shortener_url)

    # Testing homepage
    def test_shortened_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    # Testing templates
    def test_shortener_listpage_template(self):
        self.assertTemplateUsed(self.response, "shorteners/list.html")

    # Testing HTML
    def test_shortener_listpage_contains_correct_html(self):
        self.assertContains(self.response, "All Urls")

    def test_shortener_listpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Hey! Why am I on this page.")

    def test_shortener_listpage_url_resolves_shortener_listpageview(self):
        view = resolve("/list")
        self.assertEqual(view.func.__name__, ShortenerListView.as_view().__name__)

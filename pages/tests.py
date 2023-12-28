# Import SimpleTestCase and reverse from django.test and django.urls respectively
from django.test import SimpleTestCase
from django.urls import reverse


# Define HomePageTest class that inherits from SimpleTestCase
class HomePageTest(SimpleTestCase):
    # Define test_url_exists_at_correct_location test method
    def test_url_exists_at_correct_location(self):
        # Make GET request to '/' and store response
        response = self.client.get("/")

        # Assert status code is 200
        self.assertEqual(response.status_code, 200)

    # Define test_url_avaliable_by_name test method
    def test_url_avaliable_by_name(self):
        # Make GET request using reverse lookup with 'home' and store response
        response = self.client.get(reverse("home"))

        # Assert status code is 200
        self.assertEqual(response.status_code, 200)

    # Define test_template_name_correct test method
    def test_template_name_correct(self):
        # Make GET request using reverse lookup with 'home' and store response
        response = self.client.get(reverse("home"))

        # Assert template used is 'home.html'
        self.assertTemplateUsed(response, "home.html")

    # Define test_template_content test method
    def test_template_content(self):
        # Make GET request using reverse lookup with 'home' and store response
        response = self.client.get(reverse("home"))

        # Assert response contains '<h1>Homepage</h1>'
        self.assertContains(response, "<h1>Homepage</h1>")


# Define AboutPageTest class that inherits from SimpleTestCase
class AboutPageTest(SimpleTestCase):
    # Define test_url_exists_at_correct_location test method
    def test_url_exists_at_correct_location(self):
        # Make GET request to '/about/' and store response
        response = self.client.get("/about/")

        # Assert status code is 200
        self.assertEqual(response.status_code, 200)

    # Define test_url_avaliable_by_name test method
    def test_url_avaliable_by_name(self):
        # Make GET request using reverse lookup with 'about' and store response
        response = self.client.get(reverse("about"))

        # Assert status code is 200
        self.assertEqual(response.status_code, 200)

    # Define test_template_name_correct test method
    def test_template_name_correct(self):
        # Make GET request using reverse lookup with 'about' and store response
        response = self.client.get(reverse("about"))

        # Assert template used is 'about.html'
        self.assertTemplateUsed(response, "about.html")

    # Define test_template_content test method
    def test_template_content(self):
        # Make GET request using reverse lookup with 'about' and store response
        response = self.client.get(reverse("about"))

        # Assert response contains '<h1>About Page</h1>'
        self.assertContains(response, "<h1>About Page</h1>")

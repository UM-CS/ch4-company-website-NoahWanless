from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/") #loads/ checks the url to see if it exists
        self.assertEqual(response.status_code,200) 
    
    def test_url_available_by_name(self): #tests if the internal name shortcuts still work as indented
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200) 

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response,"home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response,"<h1>Company Homepage</h1>")


class AboutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/") 
        self.assertEqual(response.status_code,200) 

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code,200) 

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response,"about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response,"<h1>Company About Page</h1>")

class ProductspageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/products/") 
        self.assertEqual(response.status_code,200) 

    def test_url_available_by_name(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code,200) 

    def test_template_name_correct(self):
        response = self.client.get(reverse("products"))
        self.assertTemplateUsed(response,"products.html")

    def test_template_content(self):
        response = self.client.get(reverse("products"))
        self.assertContains(response,"<h1>Products Page</h1>")
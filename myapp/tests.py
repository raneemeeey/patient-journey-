
from django.test import TestCase
from django.urls import reverse


class PatientJourneyTests(TestCase):

    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "myapp/home.html")

    def test_plastic_surgery_page(self):
        response = self.client.get(
            reverse("subspecialties", args=["plastic"])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "myapp/subspecialties.html"
        )

    def test_hand_surgery_page(self):
        response = self.client.get(
            reverse("surgeries", args=["hand"])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "myapp/surgeries.html"
        )

    def test_flexor_tendon_journey(self):
        response = self.client.get(
            reverse(
                "surgery_detail",
                args=["flexor-tendon-zone-5"]
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "myapp/surgery_detail.html"
        )

from django.test import TestCase, Client
from rest_framework.test import APIClient
from simple_product.models import Product
from users.models import CustomUser
from django.urls import reverse
from rest_framework.authtoken.models import Token
from decimal import Decimal


class TestProductListAPIView(TestCase):
    def setUp(self) -> None:
        self.user = CustomUser.objects.create(
            phone_number="1",
            password="1",
        )
        self.client = APIClient()
        self.product = Product.objects.create(title="Test product", text="Test text", price=100, count=10)
        self.token = self.get_user_token()

    def get_user_token(self):
        token = Token.objects.create(user=self.user)
        return token.key

    def test_get_list(self):
        response = self.client.get(reverse("product:product_list"), HTTP_AUTHORIZATION=f"Token {self.token}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        print(response.data["results"][0].keys())
        self.assertEqual(list(response.data["results"][0].keys()),
                         ['id', 'category', 'title', 'slug', 'text', 'main_image', 'price', 'count', 'images',
                          'total_amount'])
        self.assertEqual(response.data["results"][0]['price'], '100.00')

    def test_get_retrieve(self):
        response = self.client.get(reverse("product:product_detail", kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 10)

    def test_get_destroy(self):
        response = self.client.delete(reverse("product:product_destroy", kwargs={"pk": self.product.id}))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Product.objects.filter(id=self.product.id).exists())

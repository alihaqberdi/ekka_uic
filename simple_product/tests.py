from django.test import TestCase
from users.models import CustomUser


class TestAllProduct(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            phone_number="1",
            password="1",
        )

    def test_custom_user(self):
        self.assertEqual(self.user.phone_number, "1")
        users = CustomUser.objects.all()
        self.assertIn(1, [1, 2, 3])
        self.assertEqual(len(users), 1)

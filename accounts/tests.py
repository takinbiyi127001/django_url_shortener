from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username="admin",
         email="admin@email.com", password="testpassword")
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.email, "admin@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="adminsuper",
            email="adminsuper@email.com",
            password="testpassword",
        )
        self.assertEqual(admin_user.username, "adminsuper")
        self.assertEqual(admin_user.email, "adminsuper@email.com")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)
       

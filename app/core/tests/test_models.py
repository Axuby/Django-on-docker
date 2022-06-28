from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'azubuinesamuel@gmail.com'
        password = 'Test-pass12'
        user = get_user_model().objects.create_user(email=email, password=password)
        print(user)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the new user email is normalized """
        email = 'azubuinesamuel@gmail.com'
        user = get_user_model().objects.create_user(email, 'test123')
        print(user)
        self.assertEqual(user.email, email.lower())

    def test_create_new_superuser(self):
        """ Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'azubuinesamuel@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_user_invalid_email(self):
        """Test creating email address raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')

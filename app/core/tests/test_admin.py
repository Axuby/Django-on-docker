from django.test import TestCase, Client  # allow us make test requests to our app from the unit test
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """setup function, pre-run functions before every test that we run in Tstcase class"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='azubuinesamuel@gmail.com',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_superuser(
            email='azubuinesamuel@gmail.com',
            password='password123',
            name='Test user fullname',
        )

        # here we are using email as the username thus we need to modify our admin.py
        # to support our custom user model

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

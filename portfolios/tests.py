from django.test import TestCase
from models import Portfolio
from django.contrib.auth.models import User

class PortfolioTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user('test', 'test@test.com', '1234')
        user2 = User.objects.create_user('demo', 'demo@demo.com', '1234')

        Portfolio.objects.create(name="Test 1", user=user1)
        Portfolio.objects.create(name="Test 2", user=user2)

    
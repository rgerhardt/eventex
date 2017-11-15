from datetime import datetime

from django.test import TestCase

from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Mario Santos',
            cpf='12345678901',
            email='mario@eventex.net',
            phone='21-99991190'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Mario Santos', str(self.obj))

    def test_default_paid_status_should_be_False(self):
        self.assertEqual(False, self.obj.paid)
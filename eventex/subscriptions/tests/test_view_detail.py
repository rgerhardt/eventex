from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Mario Tesla',
            cpf='12345678901',
            email='mario@luigi.net',
            phone='21-99999-9999'
        )

        self.resp = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp,
            'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for text in contents:
                self.assertContains(self.resp, text)


class SubscriptionDetailNotFound(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Mario Tesla',
            cpf='12345678901',
            email='mario@luigi.net',
            phone='21-99999-9999'
        )


    def test_not_found(self):
        self.resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, self.resp.status_code)
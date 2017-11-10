from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Mario Tesla', cpf='12345678901',
                    email='mario@luigi.net', phone='21-99999-9999')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_send_subscribe_email_subject(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_email(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'mario@luigi.net']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['Mario Tesla', '12345678901', 'mario@luigi.net', '21-99999-9999']

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
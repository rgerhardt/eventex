from unittest.mock import Mock
from unittest import mock

from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionModelAdmin, Subscription, admin


class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name='Mario Santos',
            cpf='12345678901',
            email='mario@eventex.net',
            phone='21-99991190'
        )

        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_mask_as_paid_action(self):
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all_as_paid(self):
        self.call_mark_as_paid_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_send_a_message_to_user(self):
        mock = self.call_mark_as_paid_action()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')


    @mock.patch('django.contrib.admin.ModelAdmin.message_user')
    def call_mark_as_paid_action(self, mock_message_user):
        queryset = Subscription.objects.all()

        self.model_admin.mark_as_paid(None, queryset)

        return mock_message_user

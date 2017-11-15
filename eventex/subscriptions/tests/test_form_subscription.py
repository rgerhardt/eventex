from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_has_only_digits(self):
        form = self.make_validated_form(cpf='ABCDE5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='8901')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_captalized(self):
        form = self.make_validated_form(name='MARIO santos')
        self.assertEqual('Mario Santos', form.cleaned_data['name'])

    def test_email_is_optional(self):
        form = self.make_validated_form(email='')
        self.assertEqual(0, len(form.errors))

    def test_phone_is_optional(self):
        form = self.make_validated_form(phone='')
        self.assertEqual(0, len(form.errors))

    def test_must_inform_email_or_phone(self):
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))


    def make_validated_form(self, **kwargs):
        valid = dict(
            name='Mario Santos',
            cpf='12345678901',
            email='mario@eventex.net',
            phone='21-99991190'
        )

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def assertFormErrorMsg(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertEqual([msg], errors_list)

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)
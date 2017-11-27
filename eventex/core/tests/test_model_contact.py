from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

    def test_create_email_contact(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net'
        )

        self.assertTrue(Contact.objects.exists())

    def test_create_phone_contact(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='21-988448585'
        )

        self.assertTrue(Contact.objects.exists())

    def test_invalid_kind_should_raise_validation_error(self):
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='henrique@bastos.net')
        self.assertEqual('henrique@bastos.net', str(contact))


class ContactModelTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='henrique@bastos.net')
        s.contact_set.create(kind=Contact.PHONE, value='21-99999999')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['henrique@bastos.net']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['21-99999999']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
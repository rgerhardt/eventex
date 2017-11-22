from django import forms
from django.forms import ValidationError

from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'cpf',  'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.title()

    def clean(self):
        self.cleaned_data = super().clean()
        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu e-mail ou telefone')

        return self.cleaned_data
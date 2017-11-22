from django.forms import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('O cpf deve conter somente números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')
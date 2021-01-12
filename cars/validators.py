from django.core.exceptions import ValidationError
from datetime import datetime


def validate_year(value: str):
    if not value.isnumeric() or len(value) != 4:
        raise ValidationError('Enter a valid year!')
    if 1900 > int(value) or datetime.now().year < int(value):
        raise ValidationError(f'The car can\'t have been made in {value}')

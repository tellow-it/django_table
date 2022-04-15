from django import forms
from .models import Table


class TableForm(forms.Form):

    CHOICES_COLUMN = (
        (1, 'Name'),
        (2, 'Number'),
        (3, 'Distance'),
    )
    CHOICES_CONDITION = (
        ('equal', '=='),
        ('more', '>'),
        ('less', '<'),
    )

    column = forms.ChoiceField(choices=CHOICES_COLUMN)
    condition = forms.ChoiceField(choices=CHOICES_CONDITION)
    value = forms.CharField()


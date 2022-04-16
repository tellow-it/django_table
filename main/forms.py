from django import forms
from .models import Table


class TableForm(forms.Form):
    CHOICES_COLUMN = (
        (0, '----'),
        (1, 'Name'),
        (2, 'Number'),
        (3, 'Distance'),
    )
    CHOICES_CONDITION = (
        ('empty', '----'),
        ('equal', '=='),
        ('more', '>'),
        ('less', '<'),
        ('contains', 'in')
    )

    column = forms.ChoiceField(choices=CHOICES_COLUMN, required=True)
    condition = forms.ChoiceField(choices=CHOICES_CONDITION, required=True)
    value = forms.CharField(required=False)

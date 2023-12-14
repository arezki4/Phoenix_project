from django import forms
from Home.models import MentalBase

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.DateInput):
    input_type = 'time'

class MentalForm(forms.ModelForm):
    anxiety = forms.IntegerField(
        label="Évaluez votre anxiété après votre écoute",
        widget=forms.NumberInput(attrs={
            'class': 'form-range border-0',
            'type': 'range',
            'min': '0',
            'max': '10',
            'value': '5',
            'step': '1',
            'required': True
        })
    )

    depression = forms.IntegerField(
        label="Évaluez votre anxiété après votre écoute",
        widget=forms.NumberInput(attrs={
            'class': 'form-range border-0',
            'type': 'range',
            'min': '0',
            'max': '10',
            'value': '5',
            'step': '1',
            'required': True
        })
    )

    insomnia = forms.IntegerField(
        label="Evaluez votre dépression après votre écoute",
        widget=forms.NumberInput(attrs={
            'class': 'form-range border-0',
            'type': 'range',
            'min': '0',
            'max': '10',
            'value': '5',
            'step': '1',
            'required': True
        })
    )

    ocd = forms.IntegerField(
        label="Evaluez vos TOC après votre écoute",
        widget=forms.NumberInput(attrs={
            'class': 'form-range border-0',
            'type': 'range',
            'min': '0',
            'max': '10',
            'value': '5',
            'step': '1',
            'required': True
        })
    )

    class Meta:
        model = MentalBase
        fields = "__all__"
        widgets = {
            'birthdate': DateInput(),
            'hoursperday': TimeInput(),
        }

from django import forms

class MentalForm(forms.Form):
   name = forms.CharField(required=False)
   anxity_note = forms.IntegerField(min_value=0, max_value=10)
   deprecion_note = forms.IntegerField(min_value=0, max_value=10)
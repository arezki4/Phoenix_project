from django import forms

class MentalForm(forms.Form):
   FirstName = forms.CharField(required=False)
   SecondName = forms.CharField(required=False)
   Anxiety_note = forms.IntegerField(min_value=0, max_value=10)
   Depression_note = forms.IntegerField(min_value=0, max_value=10)
   insomnia_note = forms.IntegerField(min_value=0, max_value=10)
   OCD_note = forms.IntegerField(min_value=0, max_value=10)
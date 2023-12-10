from django import forms

class MentalForm(forms.Form):
   FirstName = forms.CharField(label='First Name', min_length=2, max_length=15, required=True)
   LastName = forms.CharField(label='Last Name', min_length=2, max_length=15, required=True)
   Email = forms.EmailField(label='Email', max_length=30, required=True)
   Anxiety_note = forms.IntegerField(min_value=0, max_value=10)
   Depression_note = forms.IntegerField(min_value=0, max_value=10)
   insomnia_note = forms.IntegerField(min_value=0, max_value=10)
   OCD_note = forms.IntegerField(min_value=0, max_value=10)
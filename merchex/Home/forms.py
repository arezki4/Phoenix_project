from django import forms
import pycountry

COUNTRY_CHOICES = sorted([(country.alpha_2, (country.name)) for country in pycountry.countries if not hasattr(country, 'subdivisions')], key=lambda x: x[1])
GENRE_CHOICES = [
   ('cl', 'Classique'),
   ('co', 'Country'),
   ('edm', 'EDM'),
   ('f', 'Folk'),
   ('g', 'Gospel'),
   ('hh', 'Hip Hop'),
   ('j', 'Jazz'),
   ('kp', 'Kpop'),
   ('la', 'Latin'),
   ('lo', 'Lofi'),
   ('m', 'Metal'),
   ('p', 'Pop'),
   ('r&b', 'R&B'),
   ('rap', 'RAP'),
   ('r', 'Rock'),
   ('vgm', 'Video game music')
]

PAROLE_CHOISES = [
   ('o', 'Oui'),
   ('s', 'Souvent'),
   ('n', 'Non'),
   ('r', 'Rarement')
]

class MentalForm(forms.Form):
   FirstName = forms.CharField(label='Prénom', min_length=2, max_length=15, required=False)
   LastName = forms.CharField(label='Nom', min_length=2, max_length=15, required=False)
   Email = forms.EmailField(label='Email', max_length=30, required=True)
   Age = forms.IntegerField(label='Age', min_value=13, max_value=100, required=True)
   Pays_de_residence = forms.ChoiceField(label='Pays de résidence', widget=forms.Select, choices=COUNTRY_CHOICES, required=True)
   Genre_preferer = forms.ChoiceField(label='Quel est votre genre préféré ?', widget=forms.Select, choices=GENRE_CHOICES, required=True)
   Heure_ecoute = forms.TimeField(
      label="Combien d'heures écoutez-vous de la musique par jour?",
      widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
      required=True,
   )
   Paroles = forms.ChoiceField(label='Comprenez vous les paroles des musiques que vous écoutez ?', widget=forms.Select, choices=PAROLE_CHOISES, required=True)  
   
   Anxiety_evaluation = forms.IntegerField(
        label="Évaluez votre anxiété après votre écoute",
        widget=forms.TextInput(attrs={
            'class': 'form-range border-0',
            'type': 'range',
            'min': '0',
            'max': '10',
            'value': '5',
            'step': '1',
            'required': True
        })
    )
   Depression_evaluation = forms.IntegerField(
        label="Evaluez votre dépression après votre écoute",
        widget=forms.TextInput(attrs={
            'class': 'form-range border-0',
            'type': 'range',
            'min': '0',
            'max': '10',
            'value': '5',
            'step': '1',
            'required': True
        })
    )
   insomnia_evaluation = forms.IntegerField(
        label="Evaluez votre insomnie après votre écoute",
        widget=forms.TextInput(attrs={
            'class': 'form-range border-0',
            'type': 'range',
            'min': '0',
            'max': '10',
            'value': '5',
            'step': '1',
            'required': True
        })
    )
   OCD_evaluation = forms.IntegerField(
        label="Evaluez vos TOC après votre écoute",
        widget=forms.TextInput(attrs={
            'class': 'form-range border-0',
            'type': 'range',
            'min': '0',
            'max': '10',
            'value': '5',
            'step': '1',
            'required': True
        })
    )
from django.db import models
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


class MentalBase(models.Model):
    timestamp = models.DateField(auto_now=True, verbose_name='Heure à laquelle le formulaire a été complété')
    surname = models.CharField(max_length=15, verbose_name='Prénom')
    lastname = models.CharField(max_length=15, verbose_name='Nom')
    email = models.EmailField(max_length=50, unique=True, verbose_name="Adresse mail")
    birthdate = models.DateField(verbose_name='Date de naissance')
    country = models.CharField(max_length=2, choices=COUNTRY_CHOICES,verbose_name='Pays de résidence')
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES,verbose_name='Quel est votre genre préféré ?')
    hoursperday = models.TimeField(verbose_name='Combien d\'heures écoutez-vous de la musique par jour ?')
    foreign = models.CharField(max_length=1, choices=PAROLE_CHOISES,verbose_name='Comprenez vous les paroles des musiques que vous écoutez ?')
    anxiety = models.IntegerField(default=5, verbose_name='évaluation du degré d\'anxiété après écoute')
    depression = models.IntegerField(default=5, verbose_name='évaluation du degré de dépression après écoute')
    insomnia = models.IntegerField(default=5, verbose_name='évaluation du degré d\'insomnie après écoute')
    ocd = models.IntegerField(default=5, verbose_name='évaluation du degré de TOC après écoute')
    form_del = models.BooleanField(default = False)

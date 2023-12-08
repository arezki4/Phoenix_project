from django.shortcuts import render
from Home.forms import MentalForm

def mental(request):
    form = MentalForm()  # ajout d’un nouveau formulaire ici
    if (request.method == "POST"):
        form = MentalForm(request.POST)
    return render(request, 'Home/home.html', {'form': form})  # passe ce formulaire au gabarit
from django.shortcuts import render
from Home.forms import MentalForm

def index(request):
    context = {'view_selectionne': 'index'}
    return render(request, 'Home/index.html', context)

def mental(request):
    form = MentalForm()  # ajout d’un nouveau formulaire ici
    if (request.method == "POST"):
        form = MentalForm(request.POST)
    return render(request, 'Home/form.html', {'form': form})  # passe ce formulaire au gabarit
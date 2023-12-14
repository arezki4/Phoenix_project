from django.shortcuts import redirect, render
from Home.forms import MentalForm
from datetime import timedelta
from datetime import datetime
from Home.models import MentalBase

def index(request):
    context = {'view_selectionne': 'index'}
    return render(request, 'Home/index.html', context)

def mental(request):
    message_success = ''
    message_fail = ''
    form = MentalForm()  # ajout d’un nouveau formulaire ici
    if (request.method == "POST"):
        form = MentalForm(request.POST)
        # form.save()
        if form.is_valid():
            email = form.cleaned_data['email']
            now = datetime.now()
            last_record = MentalBase.objects.filter(email=email).order_by('-timestamp').first()
            if last_record and (now.date() - last_record.timestamp) < timedelta(hours=1):
                message_fail = 'Vous avez déjà soumis un formulaire dans la dernière heure'
                return render(request, 'Home/form.html', {'message_fail': message_fail, 'message_success': message_success, 'form': form})
            else:
                message_success = 'Formulaire soumis avec succès'
            form.save()
    else:
        form = MentalForm()

    return render(request, 'Home/form.html', {'form': form, 'message_success': message_success, 'message_fail': message_fail})  # passe ce formulaire au gabarit
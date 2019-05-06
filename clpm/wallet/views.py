from django.http import HttpResponse
from django.shortcuts import render

from .models import Account

# index view
def index(request):
    context = {
        'title': "Compte | Accueil",
        'accounts': Account.objects.all()
    }
    return render(request, 'wallet/default.html', context)


def charge(request):
    context = {
        'title': "Compte | Rechargement",
    }
    return render(request, 'wallet/charge.html', context)


def spend(request):
    context = {
        'title': "Compte | Boutique",
    }
    return render(request, 'wallet/spend.html', context)
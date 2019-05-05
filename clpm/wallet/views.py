from django.http import HttpResponse
from django.shortcuts import render

from .models import Account

# index view
def index(request):
    context = {
        'accounts': Account.objects.all()
    }
    return render(request, 'wallet/default.html', context)
def charge(request):
	return render(request, 'wallet/charge.html')
def spend(request):
	return render(request, 'wallet/spend.html')

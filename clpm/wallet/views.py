from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Account

# index view
def index(request):
    request.session['current_account_id'] = -1
    context = {
        'title': "Compte | Accueil",
        'accounts': Account.objects.all()
    }
    return render(request, 'wallet/index.html', context)


# Account management main view
def account_index(request, id = -1):
    account = getAccount(request, id)

    # Check if account has been found
    if(account == None):
        redirect('index')

    # Set session
    request.session['current_account_id'] = account.id

    # Create context
    context = {
        'title': "Compte | {}".format(account.name),
        'current_account': account,
    }

    # Return the view
    return render(request, 'wallet/account.html', context)


def reload(request, id):
    # Get request processing
    if(request.method == 'GET'):
        account = getAccount(request, id)

        # Check if account has been found
        if(account == None):
            redirect('index')

        # Set session
        request.session['current_account_id'] = account.id

        context = {
            'title': "Compte | Rechargement",
            'current_account': account,
        }

    # POST request processing
    elif(request.method == 'POST'):
        pass
    
    return render(request, 'wallet/reload.html', context)


def shop(request, id):
    account = getAccount(request, id)

    # Check if account has been found
    if(account == None):
        redirect('index')

    # Set session
    request.session['current_account_id'] = account.id

    context = {
        'title': "Compte | Boutique",
        'current_account': account,
    }
    return render(request, 'wallet/shop.html', context)


'''
Utility function to get account from id, 
return None if no account found
'''
def getAccount(request, id):
    if(id == -1):
        # Check if account exists in session
        id = request.session['current_account_id']
        if(id == -1):
            # redirect to index
            return None

    account = Account.objects.get(id=id)

    # Check if account has been found
    if(account == None):
        return None

    return account
from django.http import HttpResponse
from django.template import loader

from .models import Account

# index view
def index(request):
    template = loader.get_template('wallet/default.html')
    context = {
        'accounts': Account.objects.all()
    }
    return HttpResponse(template.render(context, request))
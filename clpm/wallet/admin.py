from django.contrib import admin

from .models import Account, AccountTransaction, AccountReload

# Register your models here.
admin.site.register(Account)
admin.site.register(AccountTransaction)
admin.site.register(AccountReload)
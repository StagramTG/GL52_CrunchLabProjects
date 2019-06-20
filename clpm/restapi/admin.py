from django.contrib import admin
from restapi.models import User, Account, AccountTransaction, AccountReload, ShopProduct

# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(AccountTransaction)
admin.site.register(AccountReload)
admin.site.register(ShopProduct)
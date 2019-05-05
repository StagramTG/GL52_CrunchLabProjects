from django.db import models

# ===================================================
# These models are used to manage money in the application.
# Each user can have an account and put some money on it
# in order to afford for pieces or services relatives to
# projects.
# ===================================================


# Account class
class Account(models.Model):
    balance = models.FloatField(default=0.0)
    name = models.CharField(max_length = 255,default='account')
    
    def checkBalance(self,balance):
    	if(balance <= 0):
    		return False
    	else:
    		return True
    





# Account transaction, follow transactions on an account
class AccountTransaction(models.Model):
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    amount = models.FloatField()


# Account Reload, follow reloading operations on an account
class AccountReload(models.Model):
    account_id = models.ForeignKey('Account', on_delete=models.CASCADE)
    amount = models.FloatField()

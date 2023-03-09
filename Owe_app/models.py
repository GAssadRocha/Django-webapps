from django.db import models

# Create your models here.

class UserInfo(models.Model):
    first_name = models.CharField(max_length=30, primary_key=True)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

class Transaction(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    payer_user_name = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, related_name='Payer_User_Name')
    payee_user_name = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, related_name='Payee_User_Name')
    value = models.DecimalField(max_digits=8, decimal_places=2)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




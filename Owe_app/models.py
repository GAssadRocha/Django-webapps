from django.db import models

# Create your models here.

class UserInfo(models.Model):
    first_name = models.CharField(max_length=30, primary_key=True)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

class Transaction(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    payer_user_name = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING)
    payee_user_name = models.CharField(max_length=30)

    def __str__(self):
        return self.name




from django.db import models

class User(models.Model):
    business=models.CharField(max_length=250)
    sells_point=models.CharField(max_length=250)
    target =models.CharField(max_length=250)
    
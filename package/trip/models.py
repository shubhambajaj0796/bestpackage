from django.db import models

# Create your models here.
class tb_registration(models.Model):
    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    password = models.CharField(max_length=225)

from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=220)
    surname=models.CharField(max_length=329)
    email = models.CharField(max_length=302)
    subject=models.CharField(max_length=1002)
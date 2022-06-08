from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class arunachal_pradesh(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=5600)
    cafes = models.CharField(max_length=5600)
    image = models.ImageField(upload_to="arunachal_pradesh/",max_length=250,null=True,default=None)

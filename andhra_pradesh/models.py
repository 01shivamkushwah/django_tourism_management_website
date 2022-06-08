from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class andhra_pradesh(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=5500)
    cafes = models.CharField(max_length=5050)
    image = models.ImageField(upload_to="andhra_pradesh/",max_length=250,null=True,default=None)

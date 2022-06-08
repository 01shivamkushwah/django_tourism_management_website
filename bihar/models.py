from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class bihar(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=4500)
    cafes = models.CharField(max_length=5400)
    image = models.ImageField(upload_to="bihar/",max_length=250,null=True,default=None)

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class mizoram(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=1200)
    cafes = models.CharField(max_length=1200)
    image = models.ImageField(upload_to="mizoram/",max_length=250,null=True,default=None)

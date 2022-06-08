from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class telengana(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=13200)
    cafes = models.CharField(max_length=13200)
    image = models.ImageField(upload_to="telengana/",max_length=250,null=True,default=None)

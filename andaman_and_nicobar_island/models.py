from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class andaman_and_nicobar_island(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=4500)
    cafes = models.CharField(max_length=5004)
    image = models.ImageField(upload_to="andaman_and_nicobar_island/",max_length=250,null=True,default=None)

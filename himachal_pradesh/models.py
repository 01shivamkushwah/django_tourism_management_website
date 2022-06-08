from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class himachal_pradesh(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=1020)
    cafes = models.CharField(max_length=1200)
    image = models.ImageField(upload_to="himachal_pradesh/",max_length=250,null=True,default=None)

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class rajashtan(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=1020)
    cafes = models.CharField(max_length=1020)
    image = models.ImageField(upload_to="rajashtan/",max_length=250,null=True,default=None)

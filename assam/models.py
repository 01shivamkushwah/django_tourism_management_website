from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class assam(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=5300)
    cafes = models.CharField(max_length=5300)
    image = models.ImageField(upload_to="assam/",max_length=250,null=True,default=None)

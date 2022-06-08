from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class chattisgarh(models.Model):
    name =  models.CharField(max_length=50)
    desc =  HTMLField()
    hotels = models.CharField(max_length=5040)
    cafes = models.CharField(max_length=5040)
    image = models.ImageField(upload_to="chattisgarh/",max_length=250,null=True,default=None)

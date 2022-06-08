from django.contrib import admin
from panjab.models import panjab
# Register your models here.
class panjabAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(panjab,panjabAdmin)
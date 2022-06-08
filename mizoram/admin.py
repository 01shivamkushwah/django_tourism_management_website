from django.contrib import admin
from mizoram.models import mizoram
# Register your models here.
class mizoramAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(mizoram,mizoramAdmin)
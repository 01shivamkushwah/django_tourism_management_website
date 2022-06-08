from django.contrib import admin
from gujrat.models import gujrat
# Register your models here.
class gujratAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(gujrat,gujratAdmin)
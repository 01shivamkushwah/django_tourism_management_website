from django.contrib import admin
from sikkim.models import sikkim
# Register your models here.
class sikkimAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(sikkim,sikkimAdmin)
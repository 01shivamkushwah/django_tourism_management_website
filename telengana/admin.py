from django.contrib import admin
from telengana.models import telengana
# Register your models here.
class telenganaAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(telengana,telenganaAdmin)
from django.contrib import admin
from odisha.models import odisha
# Register your models here.
class odishaAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(odisha,odishaAdmin)
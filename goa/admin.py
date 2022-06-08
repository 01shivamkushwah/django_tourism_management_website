from django.contrib import admin
from goa.models import goa
# Register your models here.
class goaAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(goa,goaAdmin)
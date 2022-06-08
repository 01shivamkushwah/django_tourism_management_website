from django.contrib import admin
from andhra_pradesh.models import andhra_pradesh
# Register your models here.
class andhra_pradeshAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(andhra_pradesh,andhra_pradeshAdmin)
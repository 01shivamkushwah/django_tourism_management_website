from django.contrib import admin
from arunachal_pradesh.models import arunachal_pradesh
# Register your models here.
class arunachal_pradeshAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(arunachal_pradesh,arunachal_pradeshAdmin)
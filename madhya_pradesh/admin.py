from django.contrib import admin
from madhya_pradesh.models import madhya_pradesh
# Register your models here.
class madhya_pradeshAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(madhya_pradesh,madhya_pradeshAdmin)
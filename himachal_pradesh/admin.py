from django.contrib import admin
from himachal_pradesh.models import himachal_pradesh
# Register your models here.
class himachal_pradeshAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(himachal_pradesh,himachal_pradeshAdmin)
from django.contrib import admin
from famousplace.models import famousplace
# Register your models here.
class famousplaceAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(famousplace,famousplaceAdmin)
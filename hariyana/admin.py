from django.contrib import admin
from hariyana.models import hariyana
# Register your models here.
class hariyanaAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(hariyana,hariyanaAdmin)
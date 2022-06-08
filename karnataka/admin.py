from django.contrib import admin
from karnataka.models import karnataka
# Register your models here.
class karnatakaAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(karnataka,karnatakaAdmin)
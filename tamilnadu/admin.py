from django.contrib import admin
from tamilnadu.models import tamilnadu
# Register your models here.
class tamilnaduAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(tamilnadu,tamilnaduAdmin)
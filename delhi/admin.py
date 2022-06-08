from django.contrib import admin
from delhi.models import delhi
# Register your models here.
class delhiAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(delhi,delhiAdmin)
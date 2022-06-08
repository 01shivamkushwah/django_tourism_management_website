from django.contrib import admin
from manipur.models import manipur
# Register your models here.
class manipurAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(manipur,manipurAdmin)
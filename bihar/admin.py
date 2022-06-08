from django.contrib import admin
from bihar.models import bihar
# Register your models here.
class biharAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(bihar,biharAdmin)
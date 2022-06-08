from django.contrib import admin
from kerla.models import kerla
# Register your models here.
class kerlaAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(kerla,kerlaAdmin)
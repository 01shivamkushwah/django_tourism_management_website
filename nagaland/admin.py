from django.contrib import admin
from nagaland.models import nagaland
# Register your models here.
class nagalandAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(nagaland,nagalandAdmin)
from django.contrib import admin
from andaman_and_nicobar_island.models import andaman_and_nicobar_island
# Register your models here.
class andaman_and_nicobar_islandAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(andaman_and_nicobar_island,andaman_and_nicobar_islandAdmin)
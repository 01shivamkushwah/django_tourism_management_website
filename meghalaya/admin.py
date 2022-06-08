from django.contrib import admin
from meghalaya.models import meghalaya
# Register your models here.
class meghalayaAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(meghalaya,meghalayaAdmin)
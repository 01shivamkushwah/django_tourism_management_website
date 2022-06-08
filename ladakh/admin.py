from django.contrib import admin
from ladakh.models import ladakh
# Register your models here.
class ladakhAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(ladakh,ladakhAdmin)
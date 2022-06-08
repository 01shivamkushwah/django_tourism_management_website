from django.contrib import admin
from assam.models import assam
# Register your models here.
class assamAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(assam,assamAdmin)
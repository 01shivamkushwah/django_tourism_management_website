from django.contrib import admin
from maharashtra.models import maharashtra
# Register your models here.
class maharashtraAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(maharashtra,maharashtraAdmin)
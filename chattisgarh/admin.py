from django.contrib import admin
from chattisgarh.models import chattisgarh
# Register your models here.
class chattisgarhAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(chattisgarh,chattisgarhAdmin)
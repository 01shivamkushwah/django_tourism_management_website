from django.contrib import admin
from jharkhand.models import jharkhand
# Register your models here.
class jharkhandAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(jharkhand,jharkhandAdmin)
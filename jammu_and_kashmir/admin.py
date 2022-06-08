from django.contrib import admin
from jammu_and_kashmir.models import jammu_and_kashmir
# Register your models here.
class jammu_and_kashmirAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(jammu_and_kashmir,jammu_and_kashmirAdmin)
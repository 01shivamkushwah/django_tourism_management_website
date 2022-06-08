from django.contrib import admin
from rajashtan.models import rajashtan
# Register your models here.
class rajashtanAdmin(admin.ModelAdmin):
    list_display=('name','desc','hotels','cafes','image')
admin.site.register(rajashtan,rajashtanAdmin)
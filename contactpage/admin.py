from django.contrib import admin
from contactpage.models import contact
# Register your models here.
class newsAdmin(admin.ModelAdmin):
    list_display=('name','surname','email','subject')
admin.site.register(contact,newsAdmin)

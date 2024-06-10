from django.contrib import admin
from .models import ContactUs
#nicher class er madome ki ki show korbe oita thik kore diye jai.
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name','phone','problem']
    
admin.site.register(ContactUs,ContactModelAdmin)

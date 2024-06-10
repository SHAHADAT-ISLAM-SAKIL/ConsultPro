from django.contrib import admin
from . import models
# send email:
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['consulter_name', 'client_name', 'appinment_types', 'appinment_status', 'symptom', 'time', 'cancel']
    
    def client_name(self, obj):
        return obj.client.user.first_name
    
    def consulter_name(self, obj):
        return obj.consulter.user.first_name
    
    # Send an email if the appointment is running and online
    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appinment_status == "Running" and obj.appinment_types == "online":
            email_subject = "Your Online Appointment is Running"
            email_body = render_to_string('admin_email.html', {'user': obj.client.user, 'consulter': obj.consulter})
            email = EmailMultiAlternatives(email_subject, '', to=[obj.client.user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()

admin.site.register(models.Appointment, AppointmentAdmin)

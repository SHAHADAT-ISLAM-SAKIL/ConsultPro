from django.db import models
from client.models import Client
from consulter.models import Consulter, AvailableTime

# Choices for appointment status and types
APPINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
APPOINTMENT_TYPES = [
    ('offline', 'offline'),
    ('online', 'online'),
]

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    consulter = models.ForeignKey(Consulter, on_delete=models.CASCADE)
    appinment_types = models.CharField(choices=APPOINTMENT_TYPES, max_length=10)
    appinment_status = models.CharField(choices=APPINTMENT_STATUS, max_length=10, default="Pending")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Consulter: {self.consulter.user.first_name}, Client: {self.client.user.first_name}"

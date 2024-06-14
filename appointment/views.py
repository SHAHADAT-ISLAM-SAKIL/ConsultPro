from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    
    def get_queryset(self):
 
        queryset = super().get_queryset()
        print(self.request.query_params)
        client_id = self.request.query_params.get('client_id')
       
        if client_id:
            queryset = queryset.filter(client_id=client_id)
     
 
        return queryset
    
    def perform_create(self, serializer):
        serializer.save()

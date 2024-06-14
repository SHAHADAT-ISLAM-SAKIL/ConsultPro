
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import pagination ,filters




class SpecializationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly] # etar madome login kari chara ono keo data change korte parbe na.
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    
    
class DesignationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationsSerializer
    
class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        consulter_id = request.query_params.get("consulter_id")
        if consulter_id:
            return query_set.filter(consulter = consulter_id)
        return query_set
class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctor]



class ConsulterPagination(pagination.PageNumberPagination):
    page_size = 1 #items per page
    page_size_query_param = page_size
    max_page_size = 100


class ConsulterViewset(viewsets.ModelViewSet):   
    permission_classes = [IsAuthenticatedOrReadOnly]                
    pagination_class = ConsulterPagination  
    queryset = models.Consulter.objects.all()
    serializer_class = serializers.ConsulterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__email', 'designation__name', 'specialization__name']
    
class ReviewForspecificConsaltent(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        consultant_id = request.query_params.get("consultant_id")
        if consultant_id:
            return query_set.filter(consulter = consultant_id)
        return query_set
    
class ReviewViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    filter_backends = [ReviewForspecificConsaltent]
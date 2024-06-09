from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('specialization/', views.SpecializationViewset) # router er antena
router.register('review/', views.ReviewViewset) 
router.register('consulter/', views.ConsulterViewset) 
router.register('abailable_time/', views.AvailableTimeViewset) 
router.register('designation/', views.DesignationViewset) 

urlpatterns = [
    path('', include(router.urls)),
]
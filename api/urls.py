from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api.views import studentviewset
router = routers.DefaultRouter()
router.register(r'students', studentviewset)

urlpatterns = [
    path('', include(router.urls)),
  
   
]

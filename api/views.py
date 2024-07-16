from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import studentserialiser
from api.models import students
# Create your views here.
class studentviewset(viewsets.ModelViewSet):
    queryset = students.objects.all()
    serializer_class =studentserialiser
    



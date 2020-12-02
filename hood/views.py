from django.shortcuts import render
#django_framework
from rest_framework.response import Response
# from rest_framework.views import Views
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework import status
# from .permissions import IsAdminOrReadOnly

# Create your views here.

def home(request):
    
    
    return render(request, "home.html")
class NeighbourhoodViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = NeighbourhoodSerializer
    queryset = Neighbourhood.objects.all()
    
class ProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

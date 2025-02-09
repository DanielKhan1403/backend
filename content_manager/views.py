
# Create your views here.


from rest_framework import viewsets,generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import Service, PortfolioItem, TeamSection, Video,PortfolioCategory
from .serializers import ServiceSerializer, PortfolioItemSerializer, TeamSectionSerializer,VideoSerializer

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class PortfolioListView(generics.ListAPIView):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioItemSerializer

class TeamListView(generics.ListAPIView):
    queryset = TeamSection.objects.all()
    serializer_class = TeamSectionSerializer




class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



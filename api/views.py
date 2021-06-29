from rest_framework import viewsets, permissions, filters
from .models import VideoGame, Genre, Platform, Publisher
from .serializers import VideoGameSerializer, GenreSerializer, PlatformSerializer, PublisherSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class VideoGameViewSet(viewsets.ModelViewSet):

    queryset = VideoGame.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['platform__name', 'genres__name', 'publisher__trade_name']
    serializer_class = VideoGameSerializer
    permission_classes = [permissions.IsAuthenticated]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by('name')
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all().order_by('name')
    serializer_class = PlatformSerializer
    permission_classes = [permissions.IsAuthenticated]

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all().order_by('trade_name')
    serializer_class = PublisherSerializer
    permission_classes = [permissions.IsAuthenticated]
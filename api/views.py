import django_filters
from rest_framework import viewsets, permissions, filters
from .models import VideoGame, Genre, Platform, Publisher
from .serializers import VideoGameSerializer, GenreSerializer, PlatformSerializer, PublisherSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.fields import Lookup

#filtros
class ListFilter(django_filters.Filter):
    def filter(self, qs, value):

        value = value.split(u",")
        print(qs)
        return super(ListFilter, self).filter(qs, Lookup(lookup_expr="name__in", value=value))


class VideoGameFilter(django_filters.FilterSet):
    class Meta:
        model = VideoGame
        fields = {
            'name', 'published_year', 'platform', 'publisher', 'genres', 'published_year'
        }
    starts_with = django_filters.CharFilter(field_name='name', lookup_expr='istartswith')
    platform = django_filters.CharFilter(field_name='platform', lookup_expr='name__iexact')
    #genres = ListFilter(field_name="genres")
    publisher = django_filters.CharFilter(field_name='publisher', lookup_expr='trade_name__iexact')
    year = django_filters.DateFilter(field_name='published_year', lookup_expr='published_year__icontains')

# Create your views here.
class VideoGameViewSet(viewsets.ModelViewSet):

    queryset = VideoGame.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['platform__name', 'genres__name', 'publisher__trade_name', 'name']
    serializer_class = VideoGameSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_class = VideoGameFilter


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
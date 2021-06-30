import django_filters
from rest_framework import viewsets, permissions, filters, response
from .models import VideoGame, Genre, Platform, Publisher
from .serializers import VideoGameSerializer, GenreSerializer, PlatformSerializer, PublisherSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.fields import Lookup
import json


# filtros
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
    # genres = ListFilter(field_name="genres")
    publisher = django_filters.CharFilter(field_name='publisher', lookup_expr='trade_name__iexact')
    year = django_filters.DateFilter(field_name='published_year', lookup_expr='published_year__icontains')


# Create your views here.
class VideoGameViewSet(viewsets.ModelViewSet):
    queryset = VideoGame.objects.all().order_by('name')
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['platform__name', 'genres__name', 'publisher__trade_name', 'name']
    serializer_class = VideoGameSerializer
    permission_classes = [permissions.IsAuthenticated]

    # filter_class = VideoGameFilter

    def get_queryset(self):
        start_with = self.request.query_params.get('starts_with')
        platform = self.request.query_params.get('platform')
        publisher = self.request.query_params.get('publisher')
        year = self.request.query_params.get('year')
        genres = self.request.query_params.get('genres')

        #filtro para genres, entra una lista y busca en ella
        if genres is not None:
            try:
                genres = json.loads(genres)
            except json.decoder.JSONDecodeError:
                genres = None
            print(genres)
            self.queryset = self.queryset.filter(genres__name__in=genres)
        #filtro para platform
        if platform is not None:
            print(platform)
            self.queryset = self.queryset.filter(platform__name__iexact=platform)
        #filtro para publisher
        if publisher is not None:
            print(publisher)
            self.queryset = self.queryset.filter(publisher__trade_name__iexact=publisher)
        #filtro de published_year
        if year is not None:
            print(year)
            self.queryset = self.queryset.filter(published_year__contains=year)
        if start_with is not None:
            print(start_with)
            self.queryset = self.queryset.filter(name__istartswith=start_with)



        return self.queryset


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

from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text

from .models import VideoGame, Genre, Platform, Publisher
from rest_framework import serializers

class GenreRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        data = data.lower()
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class VideoGameSerializer(serializers.ModelSerializer):
    genres = GenreRelatedField(
        many=True,
        slug_field='name',
        queryset=Genre.objects.all()
    )

    publisher = serializers.SlugRelatedField(many=False, slug_field='trade_name', queryset=Publisher.objects.all())
    platform = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Platform.objects.all())
    class Meta:
        model = VideoGame
        fields = ['name', 'published_year', 'genres', 'publisher', 'platform', 'created_at', 'updated_at']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'description', 'created_at', 'updated_at']

    def create(self, validated_data):
        name = validated_data.pop('name').lower()
        instance = Genre(**validated_data, name=name)
        instance.save()
        return instance

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['name', 'manufacturer', 'created_at', 'updated_at']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['trade_name', 'founded', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super(PublisherSerializer, self).to_representation(instance)
        data.update(...)
        return data





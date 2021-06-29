from django.db import models


# Create your models here.

class Genre(models.Model):
    class Meta:
        db_table = "genres"

    name = models.CharField(unique=True, max_length=64)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Platform(models.Model):
    class Meta:
        db_table = "platforms"

    name = models.CharField(unique=True, max_length=64)
    manufacturer = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Publisher(models.Model):
    class Meta:
        db_table = "publishers"

    trade_name = models.CharField(unique=True, max_length=64)
    founded = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.trade_name)

class VideoGame(models.Model):
    class Meta:
        db_table = "videogames"

    name = models.CharField(max_length=64)
    published_year = models.IntegerField()
    genres = models.ManyToManyField(Genre, null=True, related_name="games")
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, related_name="games")
    platform = models.ManyToManyField(Platform, null=True, related_name="games")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

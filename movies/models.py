# from django.conf import settings
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Genre(models.Model):

    # Properties
    name = models.CharField(max_length=250, unique=True)

    # Functions
    def __str__(self):
        return self.name

    # class Meta:
    #     pass


class Movie(models.Model):
    # Properties
    name = models.CharField(max_length=250, unique=False)
    director = models.CharField(max_length=250, unique=False)
    imdb_score = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(11)])
    popularity99 = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(101)])
    genres = models.ManyToManyField(Genre)

    # Functions
    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'director'),)



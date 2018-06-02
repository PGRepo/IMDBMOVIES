from rest_framework import serializers
from .models import Movie, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = 'name'


class MovieCreateSerializer(serializers.ModelSerializer):
    genres = serializers.ListField(write_only=True)

    class Meta:
        model = Movie
        # fields = ('movie_id', 'name', 'director', 'imdb_score', 'popularity99', 'genre')
        fields = '__all__'

    def create(self, validated_data):
        genre_data = validated_data.pop('genres')
        movie = Movie.objects.create(**validated_data)
        for genre in genre_data:
            genre, created = Genre.objects.get_or_create(name=genre)
            movie.genres.add(genre)
        return movie

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.popularity99 = validated_data.get('popularity99', instance.popularity99)
        instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
        instance.director = validated_data.get('director', instance.director)
        instance.genre = []
        for genre in validated_data['genres']:
            genre, created = Genre.objects.get_or_create(name=genre)
            instance.genres.add(genre)
        instance.save()
        return instance


class MovieMainSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ('name', 'director','imdb_score', 'popularity99', 'genres')
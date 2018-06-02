from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Movie, Genre
from .serializers import MovieMainSerializer, MovieCreateSerializer, GenreSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import generics

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieMainSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create' or 'update':
            return MovieCreateSerializer
        return MovieMainSerializer


class MovieByName(APIView):

    def get_queryset(self):

        name = self.request.query_params.get('name')

        queryset = Movie.objects.filer(name=name)

        return queryset

    def get(self, request, name):
        if name:
            movies = Movie.objects.filter(name=name)
            serialized_data = MovieMainSerializer(movies, many=True)
            return Response(serialized_data.data)

class MovieByName(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MovieMainSerializer

    def get_queryset(self):
        return Movie.objects.all()

    def get_object(self):
        name =self.kwargs.get("name")
        return Movie.objects.get(pk=name)


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


from django.urls import path, include
from . import views
from rest_framework import routers
from django.conf.urls import url



router = routers.DefaultRouter()
# define endpoint and the view target

router.register('movies', views.MovieView)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^movies/search/(?P<name>\w+)/$', views.MovieByName.as_view)
]



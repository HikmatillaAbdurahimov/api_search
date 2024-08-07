from django.urls import path
from .views import ArtistAPIViewSet,AlbomAPiView,SongsAPIView,SongDetailApiView,AlbomDetailApiView,ArtistDetailApiView

urlpatterns=[
    path('artist/', ArtistAPIViewSet.as_view(),name='artist'),
    path('albom/',AlbomAPiView.as_view(),name='albom'),
    path('song/',SongsAPIView.as_view(),name='song'),
    path('song/<int:id>/',SongDetailApiView.as_view(),name='song-detail'),
    path('albom/<int:id>/',AlbomDetailApiView.as_view(),name='albom-detail'),
    path('artist/<int:id>/',ArtistDetailApiView.as_view(),name='artist-detail'),
    ]



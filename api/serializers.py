from .models import Albom,Artist,Songs
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields=('id','first_name','last_name','username','create_at')


class AlbomSerializer(serializers.ModelSerializer):
    artist=ArtistSerializer()
    class Meta:
        model=Albom
        fields=('id','title','artist')


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Songs
        fields=('title','albom')



from django.shortcuts import render
from .models import Albom,Artist,Songs
from rest_framework.views import APIView
from .serializers import ArtistSerializer,AlbomSerializer,SongsSerializer
from rest_framework.response import Response
from rest_framework import status


#                               ARTIST

class ArtistAPIViewSet(APIView):
    def get_queryset(self):
        return Artist.objects.all()

    def get(self, request):
        artist = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            artist = artist.filter(first_name__icontains=search_data) | artist.filter(last_name__icontains=search_data)

        serializer = ArtistSerializer(artist, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer =ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        context_error = {
            "status": 400,
            "data": serializer.data,
            "message": "error"
        }
class ArtistDetailApiView(APIView):
    def get(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
        except:
            context_error = {
                "status": 404,
                "message": "error"
            }
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

        if artist:
            serializer = ArtistSerializer(artist)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            context_error = {
                "status": 404,
                "message": "error"
            }
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        artist = Artist.objects.get(id=id)
        artist.delete()
        context = {"status": 200, "massage": "Songs delete"}
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)


#                           ALBOM


class AlbomAPiView(APIView):
    def get_queryset(self):
        return Albom.objects.all()

    def get(self, request):
        albom = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            albom = albom.filter(title__icontains=search_data)

        serializer = AlbomSerializer(albom, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = AlbomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        context_error = {
            "status": 400,
            "data": serializer.data,
            "message": "error"
        }

class AlbomDetailApiView(APIView):
    def get(self, request, id):
        try:
            alboms = Albom.objects.get(id=id)
        except:
            context_error = {
                "status": 404,
                "message": "error"
            }
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

        if alboms:
            serializer = AlbomSerializer(alboms)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            context_error = {
                "status": 404,
                "message": "error"
            }
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        alboms = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=alboms, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        alboms = Albom.objects.get(id=id)
        serializer = AlbomSerializer(instance=alboms, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        alboms = Albom.objects.get(id=id)
        alboms.delete()
        context = {"status": 200, "massage": "Songs delete"}
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)


#                            SONGS


class SongsAPIView(APIView):
    def get_queryset(self):
        return Songs.objects.all()

    def get(self, request):
        song = self.get_queryset()
        search_data = request.query_params.get('search')
        if search_data is not None:
            song = song.filter(albom__icontains=search_data)| song.filter(title__icontains=search_data)

        serializer = SongsSerializer(song, many=True)
        return Response(data=serializer.data)
    def post(self,request):
        serializer=SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        context_error={
            "status":400,
            "data":serializer.data,
            "message":"error"
            }

        return  Response(data=context_error,status=status.HTTP_400_BAD_REQUEST)
class SongDetailApiView(APIView):
    def get(self,request,id):
        try:
            song = Songs.objects.get(id=id)
        except:
            context_error = {
                "status": 404,
                "message": "error"
            }
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

        if song:
            serializer = SongsSerializer(song)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            context_error = {
                "status": 404,
                "message": "error"
            }
            return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id):
        song=Songs.objects.get(id=id)
        serializer=SongsSerializer(instance=song,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self ,request,id):
        song = Songs.objects.get(id=id)
        serializer = SongsSerializer(instance=song, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        song=Songs.objects.get(id=id)
        song.delete()
        context={"status":200,"massage":"Songs delete"}
        return Response(data=context,status=status.HTTP_204_NO_CONTENT)








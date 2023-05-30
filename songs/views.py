from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

@api_view(['GET'])
def song_list(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET': # Gets a list of all songs
        serializer = SongSerializer(song)
        return Response(serializer.data)
        
    elif request.method == 'PUT': # Updates a specific song entry by id
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE': # Deletes a specific song entry by id
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def song_create(request): # Handles creation of a new Song entry
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# TODO: Add the ability to “like” a song through the web API and have the number of likes saved in the database with the song. 
# TODO: Use Postman to make a POST, PUT, DELETE, and both GET requests (get by id and get all) request to my REST web API, save it to a collection, and then export it as a JSON from Postman.
# TODO: Create an ERD for the API’s Model, showing proper fieldtypes.
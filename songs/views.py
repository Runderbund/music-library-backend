from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song

@api_view(['GET'])
def song_list(request):
    """
    List all songs
    """
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    """
    Retrieve, update or delete a song by id/pk.
    """
    song = get_object_or_404(Song, pk=pk)
    if request.method == 'GET': 
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def song_create(request):
    """
    Create a new song
    """
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def song_like(request, pk):
    """
    Increase likes of a song by id/pk
    """
    song = get_object_or_404(Song, pk=pk)
    song.likes += 1
    song.save()
    return Response({'likes': song.likes})

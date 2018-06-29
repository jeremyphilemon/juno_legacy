from django.db.models import Q

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from playlist.api.serializers import playlistSerializer
from playlist.models import Song


class playlistCLS(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = playlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        playlist = Song.objects.filter(archived=False).order_by('-date')
        return playlist

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class playlistRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = playlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Song.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class songHeart(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = playlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Song.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def patch(self, request, pk, *args, **kwargs):
        song = Song.objects.get(pk=pk)
        current_hearts = song.hearts
        song.hearts = current_hearts+1
        song.save();
        serializer = playlistSerializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.partial_update(request, *args, **kwargs)


class songView(generics.RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = playlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Song.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def patch(self, request, pk, *args, **kwargs):
        song = Song.objects.get(pk=pk)
        current_views = song.plays
        song.plays = current_views+1
        song.save();
        serializer = playlistSerializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return self.partial_update(request, *args, **kwargs)







from django.db.models import Q

from rest_framework import generics, mixins

from blog.api.serializers import storySerializer
from blog.models import Story


class storyCLS(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = storySerializer

    def get_queryset(self):
        stories = Story.objects.all().order_by('pk')
        search_query = self.request.GET.get("search")
        if search_query is not None:
            stories = stories.filter(Q(title__icontains=search_query) | Q(story__icontains=search_query)).distinct()
        return stories

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class storyRUD(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = storySerializer

    def get_queryset(self):
        return Story.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

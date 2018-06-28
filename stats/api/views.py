from django.db.models import Q

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from stats.api.serializers import changelogSerializer
from stats.models import Changelog


class changelogCLS(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = changelogSerializer

    def get_queryset(self):
        changelogs = Changelog.objects.filter(archived=False).order_by('-date')
        return changelogs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
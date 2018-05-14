from django.utils import timezone
from django.db import models
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse


class Story(models.Model):
    title = models.CharField(max_length=180, blank=False, null=False)
    story = models.TextField(blank=False)
    date = models.DateTimeField(default=timezone.now)
    archived = models.NullBooleanField(default=False)

    class Meta(object):
        verbose_name_plural = 'Stories'

    def get_api_url(self, request=None):
        return api_reverse("story-rud", kwargs={'pk': self.pk}, request=request)

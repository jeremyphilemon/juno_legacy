from django.db import models
from django.urls import reverse
from django.utils import timezone

from rest_framework.reverse import reverse as api_reverse


class Changelog(models.Model):
    title = models.CharField(max_length=180, blank=False, null=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    archived = models.NullBooleanField(default=False)

    class Meta(object):
        verbose_name_plural = 'Changelogs'

    def get_api_url(self, request=None):
        return api_reverse("changelog-cls", kwargs={'pk': self.pk}, request=request)
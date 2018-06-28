from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse as api_reverse


class Song(models.Model):
    title = models.CharField(max_length=180, blank=False, null=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=500, blank=False, null=False)
    art = models.CharField(max_length=500, blank=False, null=False)
    archived = models.NullBooleanField(default=False)

    def get_api_url(self, request=None):
        return api_reverse("playlist-rud", kwargs={'pk': self.pk}, request=request)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
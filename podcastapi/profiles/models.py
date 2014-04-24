from django.db import models
from django.contrib.auth.models import User

from podcasts.models import Podcast


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    podcasts = models.ManyToManyField(Podcast, related_name='podcasts')

    def __unicode__(self):
        return u'{0}'.format(self.user)

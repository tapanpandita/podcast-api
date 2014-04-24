from rest_framework import viewsets

from .models import Podcast
from .serializers import PodcastSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    model = Podcast
    serializer_class = PodcastSerializer
    authentication_classes = ()
    permission_classes = ()

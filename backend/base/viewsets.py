from rest_framework import viewsets, permissions, authentication
from .models import GlobalSettings
from .serializers import GlobalSettingsSerializer


class GlobalSettingsViewSet(viewsets.ModelViewSet):
    queryset = GlobalSettings.objects.all()
    serializer_class = GlobalSettingsSerializer
    pagination_class = None
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

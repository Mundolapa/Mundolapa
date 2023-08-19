from django.urls import path, include
from .viewsets import GlobalSettingsViewSet

app_name = "base"

urlpatterns = [
    path('', GlobalSettingsViewSet.as_view({'get': 'list'})),
]
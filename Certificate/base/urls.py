from django.urls import path
from .views import download_certificate

urlpatterns = [
    path('download/<str:certificate_id>/', download_certificate, name='download_certificate'),
]

"""
URL configuration for Certificate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from base.views import download_certificate, verify_certificate, my_certificates, user_login
import django.contrib.auth.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('download/<str:certificate_id>/', download_certificate, name='download_certificate'),
    path('verify/', verify_certificate, name='verify_certificate'),
    path('accounts/login/', user_login, name='user_login'),
    path('', my_certificates, name='my_certificates'),
    re_path(r'^logout/$', django.contrib.auth.views.LogoutView.as_view(),  {'next_page': '/'}, name='logout'),
]
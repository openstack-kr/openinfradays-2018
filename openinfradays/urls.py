"""openinfradays URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import path

from .views import index, ProgramList, schedule_page, login, process_login

urlpatterns = [
    url(r'^$', index),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^index.html', index, name='index'),
    url(r'^programs', ProgramList.as_view()),
    url(r'^schedule', schedule_page),
    url(r'^login/$', login),
    url(r'^login/process/(?P<token>[a-z0-9\-]+)$', process_login),
    path('admin/', admin.site.urls),

    # For flatpages
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^(?P<url>.*/)$', views.flatpage, name='flatpage'),
]

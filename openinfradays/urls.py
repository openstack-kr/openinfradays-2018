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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.flatpages import views
from django.urls import path

from .views import index, ProgramList, schedule_page, login, process_login, \
    HandOnLabList, ProgramDetail, sponsors, SponsorDetail


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    url(r'^$', index, name='index'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^index.html', index, name='index_html'),
    url(r'^sponsors.html', sponsors, name='sponsors'),
    url(r'^programs', ProgramList.as_view(), name="programs"),
    url(r'^program/(?P<pk>\d+)$', ProgramDetail.as_view(), name='program'),
    url(r'^sponsor/(?P<slug>\w+)$', SponsorDetail.as_view(), name='sponsor'),
    url(r'^schedule', schedule_page),
    url(r'^hand-on-lab', HandOnLabList.as_view()),
    url(r'^login/$', login),
    url(r'^login/process/(?P<token>[a-z0-9\-]+)$', process_login),
    path('admin/', admin.site.urls),

    url(r'^registration/', include('registration.urls')),

    # For flatpages
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^(?P<url>.*/)$', views.flatpage, name='flatpage'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
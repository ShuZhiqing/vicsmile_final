"""Vicsmile_V5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views import static
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import handler404, handler500, handler403, handler400
from home import views as home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('clinic/', include('clinic.urls')),
    path('diet/', include('diet.urls')),
    path('healthcare/', include('healthcare.urls')),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]

handler400 = home.error_400
handler403 = home.error_403
handler404 = home.error_404
handler500 = home.error_500

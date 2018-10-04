from django.urls import path,include
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.password, name='password'),
    path('about', views.about, name='about'),
    path('faq', views.faq, name='faq'),
    path('terms', views.terms, name='terms'),
    path('privacy', views.privacy, name='privacy'),
    path('copyright', views.copyright, name='copyright'),
]


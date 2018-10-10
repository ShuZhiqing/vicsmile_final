from django.urls import path
from . import views


urlpatterns = [
    path(r'diet', views.personalinfo, name='diet'),
    path(r'diet/result', views.calculate, name='dietresult'),
    path(r'china', views.china, name='china'),
    path(r'india', views.india, name='india'),
    path(r'italy', views.italy, name='italy'),
    path(r'iraq', views.iraq, name='iraq'),
    path(r'vietnam', views.vietnam, name='vietnam'),
]
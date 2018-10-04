from django.urls import path


from . import views


urlpatterns = [
    path(r'result', views.search, name='result'),
]
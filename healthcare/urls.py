from django.urls import path
from . import views


urlpatterns = [
    path(r'refugee', views.refugee, name='refugee'),
    path(r'student', views.student, name='student'),
    path(r'worker', views.worker, name='worker'),
    path(r'resident', views.resident, name='resident'),
    path(r'medicare', views.medicare, name='medicare'),
    path(r'insurance', views.insurance, name='insurance'),
    path(r'language', views.language, name='language'),
    path(r'agreement', views.agreement, name='agreement'),

]
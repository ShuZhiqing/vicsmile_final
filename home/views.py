# from django.shortcuts import render
#
#
# # Create your views here.
# def home(request):
#     return render(request, 'home/home.html', context={})
#
from django.shortcuts import render
from clinic.models import Postcode
from healthcare.urls import *

# Create your views here.
# def home(request):
#     return render(request, 'home/home.html', context={})


def home(request):

    template_name = 'home/home.html'
    location_list = Postcode.objects.all()
    queryset = {
        'address': location_list
    }
    return render(request, template_name, queryset)


def password(request):
    return render(request, 'home/password.html', context={})


def error_400(request):
    return render(request, 'home/400.html', context={})


def error_403(request):
    return render(request, 'home/403.html', context={})


def error_404(request):
    return render(request, 'home/404.html', context={})


def error_500(request):
    return render(request, 'home/500.html', context={})


def about(request):
    return render(request, 'home/about.html', context={})


def faq(request):
    return render(request, 'home/faq.html', context={})


def copyright(request):
    return render(request, 'home/copyright.html', context={})


def privacy(request):
    return render(request, 'home/privacy.html', context={})


def terms(request):
    return render(request, 'home/terms.html', context={})






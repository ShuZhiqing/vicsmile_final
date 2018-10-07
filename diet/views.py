from django.shortcuts import render


# Create your views here.
# def diet(request):
#     return render(request, 'diet/diet.html', context={})


def diet(request):
    return render(request, 'diet/diet_new.html', context={})

def china(request):
    return render(request, 'diet/china.html', context={})


def india(request):
    return render(request, 'diet/india.html', context={})


def italy(request):
    return render(request, 'diet/italy.html', context={})


def iraq(request):
    return render(request, 'diet/iraq.html', context={})


def vietnam(request):
    return render(request, 'diet/vietnam.html', context={})
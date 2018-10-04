from django.shortcuts import render


# Create your views here.
def refugee(request):
    return render(request, 'healthcare/refugee.html', context={})


def student(request):
    return render(request, 'healthcare/student.html', context={})


def worker(request):
    return render(request, 'healthcare/worker.html', context={})


def resident(request):
    return render(request, 'healthcare/resident.html', context={})


def medicare(request):
    return render(request, 'healthcare/medicare.html', context={})


def insurance(request):
    return render(request, 'healthcare/insurance.html', context={})


def language(request):
    return render(request, 'healthcare/language.html', context={})


def agreement(request):
    return render(request, 'healthcare/agreement.html', context={})




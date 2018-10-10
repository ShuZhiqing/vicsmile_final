from django.shortcuts import render
from .models import VitaminA, VitaminB6, VitaminB12, VitaminC, VitaminD, Phosphorus, Protein, Sugar, Calcium
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def personalinfo(request):
    return render(request, 'diet/diet_personalinfo.html', context={})


@csrf_exempt
def calculate(request):

    if request.method == 'POST':

        age = request.POST.get('age', '')

        gender = request.POST.get('gender', '')

        pregnant = request.POST.get('pregnant', '')

        lactating = request.POST.get('lactating', '')

        if gender == "Male":

            vitaminA = VitaminA.objects.get(age__icontains=age).male

            vitaminB6 = VitaminB6.objects.get(age__icontains=age).male

            vitaminB12 = VitaminB12.objects.get(age__icontains=age).male

            vitaminC = VitaminC.objects.get(age__icontains=age).male

            vitaminD = VitaminD.objects.get(age__icontains=age).male

            phosphorus = Phosphorus.objects.get(age__icontains=age).male

            protein = Protein.objects.get(age__icontains=age).male

            sugar = Sugar.objects.get(age__icontains=age).male

            calcium = Calcium.objects.get(age__icontains=age).male

        else:
            if pregnant == "Yes":
                vitaminA = VitaminA.objects.get(age__icontains=age).pregnancy

                vitaminB6 = VitaminB6.objects.get(age__icontains=age).pregnancy

                vitaminB12 = VitaminB12.objects.get(age__icontains=age).pregnancy

                vitaminC = VitaminC.objects.get(age__icontains=age).pregnancy

                vitaminD = VitaminD.objects.get(age__icontains=age).pregnancy

                phosphorus = Phosphorus.objects.get(age__icontains=age).pregnancy

                protein = Protein.objects.get(age__icontains=age).pregnancy

                sugar = Sugar.objects.get(age__icontains=age).pregnancy

                calcium = Calcium.objects.get(age__icontains=age).pregnancy

            elif lactating == "Yes":

                vitaminA = VitaminA.objects.get(age__icontains=age).lactation

                vitaminB6 = VitaminB6.objects.get(age__icontains=age).lactation

                vitaminB12 = VitaminB12.objects.get(age__icontains=age).lactation

                vitaminC = VitaminC.objects.get(age__icontains=age).lactation

                vitaminD = VitaminD.objects.get(age__icontains=age).lactation

                phosphorus = Phosphorus.objects.get(age__icontains=age).lactation

                protein = Protein.objects.get(age__icontains=age).lactation

                sugar = Sugar.objects.get(age__icontains=age).lactation

                calcium = Calcium.objects.get(age__icontains=age).lactation

            else:

                vitaminA = VitaminA.objects.get(age__icontains=age).female

                vitaminB6 = VitaminB6.objects.get(age__icontains=age).female

                vitaminB12 = VitaminB12.objects.get(age__icontains=age).female

                vitaminC = VitaminC.objects.get(age__icontains=age).female

                vitaminD = VitaminD.objects.get(age__icontains=age).female

                phosphorus = Phosphorus.objects.get(age__icontains=age).female

                protein = Protein.objects.get(age__icontains=age).female

                sugar = Sugar.objects.get(age__icontains=age).female

                calcium = Calcium.objects.get(age__icontains=age).female

        context = {
            "vitaminA": vitaminA,
            "vitaminB6": vitaminB6,
            "vitaminB12": vitaminB12,
            "vitaminC": vitaminC,
            "vitaminD": vitaminD,
            "phosphorus": phosphorus,
            "protein": protein,
            "sugar": sugar,
            "calcium": calcium,
        }

    return render(request, 'diet/diet_new.html', context)


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

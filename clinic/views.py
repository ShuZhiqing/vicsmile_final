from django.shortcuts import render
from .models import Clinics, Postcode
from math import sin, cos, sqrt, atan2, radians
from django.forms import Form, fields
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# def result(request):
#     return render(request, 'clinic/result.html', context={})
#
# def clinic(request):
#     return render(request, 'clinic/clinic.html', context={})
#
# def map(request):
#     return render(request, 'clinic/map.html', context={})
#

# The main search function.
# Users can search clinics by the combination of options.


@csrf_exempt
def search(request):
    # retrieve the clinic info from the database
    clinic_list = Clinics.objects.all().values()
    location_list = Postcode.objects.all()

    # define the template for the result page
    template = 'clinic/result.html'
    # initialize the error message attribute
    error_msg = ''

    # if the method of request is "POST"
    if request.method == 'POST':

        input_obj = InputForm(request.POST)

        language = request.POST.get('language', '')

        language2 = request.POST.get('language2', '')

        range = request.POST.get('distance', '')

        group = request.POST.get('group', '')

        destination1 = request.POST.get('destination', '')

        lat = request.POST.get('lat', '')

        lng = request.POST.get('lng', '')

        destination = Postcode.objects.filter(address__icontains=destination1).first()

        queryset_list = []

        if (lat == '') and (lng == ''):
            for c in clinic_list:
                distance = round(calculateDistance(c, destination.lat, destination.lng), 2)
                c["distance"] = distance
                if distance <= float(range):
                    if ((language in c["language"]) or (language2 in c["language"])) and (group in c["group"]):
                        queryset_list.append(c)
                        queryset_list = sorted(queryset_list, key=lambda query: query["waitingTime"])
        else:
            latitude = lat
            lngitude = lng
            for c in clinic_list:
                distance = round(calculateDistance(c, latitude, lngitude), 2)
                c["distance"] = distance
                if distance <= float(range):
                    if ((language in c["language"]) or (language2 in c["language"])) and (group in c["group"]):
                        queryset_list.append(c)
                        queryset_list = sorted(queryset_list, key=lambda query: query["waitingTime"])

        # if there are no match, return the message
        if not queryset_list:
            error_msg = 'No Results'
            clinic_list = sorted(clinic_list, key=lambda query: query["distance"])

    # return the result page
    return render(request, template, {
        'error_msg': error_msg,
        'address': location_list,
        'queryset_list': queryset_list,
        'clinic_list': clinic_list,
        'destination': destination,
        'input_obj': input_obj,
    })


def calculateDistance(destination, lat, lng):
    # approximate radius of earth in k
    r = 6373.0

    lat1 = radians(float((destination["lat"].strip())))
    lng1 = radians(float((destination["lng"].strip())))
    lat2 = radians(float(lat))
    lng2 = radians(float(lng))

    dlng = lng2 - lng1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlng / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = r * c
    return distance


class InputForm(Form):
    destination = fields.CharField(error_messages={'required': 'This field is required.'})
    language = fields.CharField()
    language2 = fields.CharField()
    distance = fields.CharField()
    group = fields.CharField()


from django.db import models

# is the model for clinics database
class Clinics(models.Model):

    name = models.CharField(max_length=50)
    region = models.CharField(max_length=10)
    electorate = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    group = models.CharField(max_length=10)
    website = models.CharField(max_length=200)
    doctors = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    monday = models.CharField(max_length=20)
    tuesday = models.CharField(max_length=20)
    wednesday = models.CharField(max_length=20)
    thursday = models.CharField(max_length=20)
    friday = models.CharField(max_length=20)
    saturday = models.CharField(max_length=20)
    sunday = models.CharField(max_length=20)
    waitingTime = models.CharField(max_length=20)
    postcode = models.CharField(max_length=4)
    lat = models.CharField(max_length=6)
    lng = models.CharField(max_length=6)

    class Meta:
        db_table = 'clinics' # set the table name

    def __str__(self):
        return self.name


class Postcode(models.Model):

    postcode = models.CharField(max_length=4)
    suburb = models.CharField(max_length=30)
    lat = models.CharField(max_length=30)
    lng = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = 'postcode'


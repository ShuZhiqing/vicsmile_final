from django.db import models

# Create your models here.


class VitaminA(models.Model):

    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'vitaminA'


class VitaminB6(models.Model):
    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'vitaminB6'


class VitaminB12(models.Model):
    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'vitaminB12'


class VitaminC(models.Model):
    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'vitaminC'


class VitaminD(models.Model):
    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'vitaminD'


class Sugar(models.Model):
    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'sugar'


class Calcium(models.Model):
    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'calcium'


class Phosphorus(models.Model):
    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'phosphorus'


class Protein(models.Model):
    age = models.CharField(max_length=50)
    male = models.CharField(max_length=10)
    female = models.CharField(max_length=10)
    pregnancy = models.CharField(max_length=10)
    lactation = models.CharField(max_length=10)

    class Meta:
        db_table = 'protein'












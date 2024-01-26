from django.db import models
import random
import os
import jdatetime
import uuid
from django_jalali.db import models as jmodels


def rand2Num():
    return random.randint(10, 99)


def randIntAnything():
    return int('7{}'.format(random.randint(123456, 999999)))


def randIntCity():
    return int('5{}'.format(random.randint(123456, 999999)))


def randIntVillage():
    return int('2{}'.format(random.randint(123456, 999999)))


def uploadToDeveloper(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('developer', filename)


def uploadToPropertyBelongPlace(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('propertyBelongPlace', filename)


def uploadToAnswerProperty(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('answerProperty', filename)


def uploadToAttachmentToPeople(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.Code}_{rand2Num()}.{ext}"
    return os.path.join('peopleBelongToPlace', filename)


def currentDateTime():
    # time = str(jdatetime.datetime.today())
    time = jdatetime.datetime.today()
    return time


def sesProduction():
    return f'{uuid.uuid4()}-{uuid.uuid4()}'


class APIKEY(models.Model):
    fUseChoices = (
        (1, 'Panel'),
        (2, 'Blog')
    )
    ApiKey = models.TextField(default=sesProduction)
    ForUse = models.IntegerField(default=1, choices=fUseChoices)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.fUseChoices[self.ForUse - 1][1]}'


class Character(models.Model):
    accChoices = (
        (1, 'Main Admin'),
        (2, 'Trustee'),
        (3, 'Responsible'),
    )
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=150)
    AccessLevel = models.IntegerField(default=1, choices=accChoices)

    def __str__(self):
        return f'{self.Name} - AL({self.AccessLevel})'


class Manager(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=100)
    Family = models.CharField(max_length=100)
    SirName = models.CharField(max_length=100)
    NaCode = models.CharField(max_length=10, blank=True, null=True)
    Phone = models.CharField(max_length=11)
    Password = models.CharField(max_length=50, default='')
    Character = models.ForeignKey(Character, on_delete=models.CASCADE)
    Session = models.CharField(default=sesProduction, max_length=200)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class LocationBelongToManager(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    LocationCode = models.IntegerField()
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class BigCity(models.Model):
    Code = models.IntegerField(default=randIntCity, primary_key=True)
    Name = models.CharField(max_length=150)
    nPopulation = models.IntegerField(default=0)
    nHousehold = models.IntegerField(default=0)
    type = models.IntegerField(default=1, editable=False)  # for location
    isDeleted = models.BooleanField(default=False)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self) -> str:
        return f'{self.Name} - {self.Code}'


class City(models.Model):
    Code = models.IntegerField(default=randIntCity, primary_key=True)
    Name = models.CharField(max_length=150)
    BigCity = models.ForeignKey(BigCity, on_delete=models.CASCADE)
    nPopulation = models.IntegerField(default=0)
    nHousehold = models.IntegerField(default=0)
    type = models.IntegerField(default=2, editable=False)  # for location
    isDeleted = models.BooleanField(default=False)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self) -> str:
        return f'{self.Name} - {self.Code}'


class CityPart(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=150)
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    type = models.IntegerField(default=3, editable=False)  # for location
    isDeleted = models.BooleanField(default=False)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self) -> str:
        return f'{self.Name} - {self.Code}'


class BigVillage(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=150)
    CityPart = models.ForeignKey(CityPart, on_delete=models.CASCADE)
    type = models.IntegerField(default=4, editable=False)  # for location
    isDeleted = models.BooleanField(default=False)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self) -> str:
        return f'{self.Name} - {self.Code}'


class Village(models.Model):
    Code = models.IntegerField(default=randIntVillage, primary_key=True)
    Name = models.CharField(max_length=150)
    isEconomic = models.BooleanField(default=False)
    nPopulation = models.IntegerField(default=0)
    nHousehold = models.IntegerField(default=0)
    Description = models.TextField(max_length=2000)
    CityCode = models.IntegerField(default=0)
    BigVillage = models.ForeignKey(BigVillage, on_delete=models.CASCADE)
    type = models.IntegerField(default=5, editable=False)  # for location
    isDeleted = models.BooleanField(default=False)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self) -> str:
        return f'{self.Name} - {self.Code}'


class Proper(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=150)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class PeopleBelongLocation(models.Model):
    Code = models.IntegerField(default=randIntVillage, primary_key=True)
    Name = models.CharField(max_length=150)
    Family = models.CharField(max_length=150)
    Proper = models.ForeignKey(Proper, on_delete=models.CASCADE)
    AttachmentFile = models.FileField(upload_to=uploadToAttachmentToPeople, blank=True, null=True)
    LocationCode = models.IntegerField(default=0)  # locationCode belong to city, bigCity, village, etc
    isPrivate = models.BooleanField(default=False)
    Description = models.TextField(max_length=1500)


class Property(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=100)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.Name}'


class SubProperty(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=100)
    Property = models.ForeignKey(Property, on_delete=models.CASCADE)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.Name} ( {self.Property.Name} )'


class PropertyBelongPlace(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    SubProperty = models.ForeignKey(SubProperty, on_delete=models.CASCADE)
    PlaceCode = models.IntegerField(default=0)
    Title = models.CharField(max_length=200)
    Description = models.TextField(max_length=2000)
    Image = models.ImageField(upload_to=uploadToPropertyBelongPlace, blank=True, null=True)
    isPrivate = models.BooleanField(default=False)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.Title} - ({self.SubProperty.Name})'


class AnswerToProperty(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    PropertyBelongPlace = models.ForeignKey(PropertyBelongPlace, on_delete=models.CASCADE)
    Manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    Content = models.TextField(max_length=2000)
    File = models.FileField(upload_to=uploadToAnswerProperty, blank=True, null=True)
    EditTime = jmodels.jDateTimeField(blank=True, null=True)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class RedundantInformation(models.Model):
    forChoices = (
        (1, 'Big City'),
        (2, 'City'),
        (3, 'City Part'),
        (4, 'Big Village'),
        (5, 'Village')
    )
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=100)
    isPrivate = models.BooleanField(default=False)
    ForLocation = models.IntegerField(default=1, choices=forChoices)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class ReInformationValue(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    RedundantInformation = models.ForeignKey(RedundantInformation, on_delete=models.CASCADE)
    LocationCode = models.IntegerField(default=0)
    Value = models.CharField(max_length=500)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class Section(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.Name} - {self.Code}'


class AccessCharacter(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Character = models.ForeignKey(Character, on_delete=models.CASCADE)
    Section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Character.Name} For {self.Section.Name}'


class ExportPropertyList(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    List = models.CharField(max_length=500)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)


class Organization(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    Name = models.CharField(max_length=200)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)

    def __str__(self):
        return f'{self.Name} - {self.Code}'


class SolutionBelongToProperty(models.Model):
    Code = models.IntegerField(default=randIntAnything, primary_key=True)
    PropertyBelongPlace = models.ForeignKey(PropertyBelongPlace, on_delete=models.CASCADE)
    Content = models.TextField(max_length=2000)
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    RegisterTime = jmodels.jDateTimeField(default=currentDateTime)



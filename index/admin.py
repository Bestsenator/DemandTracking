from django.contrib import admin
from .models import *
from django.contrib.auth import models


# Register your models here.

admin.site.unregister(models.User)
admin.site.unregister(models.Group)
admin.site.register(Manager)
admin.site.register(APIKEY)
admin.site.register(Character)
admin.site.register(BigCity)
admin.site.register(City)
admin.site.register(CityPart)
admin.site.register(BigVillage)
admin.site.register(Village)
admin.site.register(Proper)
admin.site.register(PeopleBelongLocation)
admin.site.register(Property)
admin.site.register(SubProperty)
admin.site.register(PropertyBelongPlace)
admin.site.register(AnswerToProperty)
admin.site.register(RedundantInformation)
admin.site.register(ReInformationValue)
admin.site.register(AccessCharacter)
admin.site.register(Section)
admin.site.register(ExportPropertyList)
admin.site.register(Organization)
admin.site.register(SolutionBelongToProperty)
admin.site.register(LocationBelongToManager)
admin.site.register(Slider)

import jdatetime

from .models import *
from rest_framework import serializers


class ManagerSer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = '__all__'
        depth = 2


class BigCitySer(serializers.ModelSerializer):
    class Meta:
        model = BigCity
        fields = '__all__'


class BigCityListSer(serializers.ModelSerializer):
    Type = serializers.SerializerMethodField()

    class Meta:
        model = BigCity
        fields = ['Code', 'Name', 'Type']

    @staticmethod
    def get_Type(obj):
        return 1


class CitySer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
        depth = 2


class CityListSer(serializers.ModelSerializer):
    Type = serializers.SerializerMethodField()

    class Meta:
        model = City
        fields = ['Code', 'Name', 'Type']

    @staticmethod
    def get_Type(obj):
        return 2


class CityPartSer(serializers.ModelSerializer):
    class Meta:
        model = CityPart
        fields = '__all__'
        depth = 2


class CityPartListSer(serializers.ModelSerializer):
    Type = serializers.SerializerMethodField()

    class Meta:
        model = CityPart
        fields = ['Code', 'Name', 'Type']

    @staticmethod
    def get_Type(obj):
        return 3


class BigVillageSer(serializers.ModelSerializer):
    class Meta:
        model = BigVillage
        fields = '__all__'
        depth = 3


class BigVillageListSer(serializers.ModelSerializer):
    Type = serializers.SerializerMethodField()

    class Meta:
        model = BigVillage
        fields = ['Code', 'Name', 'Type']

    @staticmethod
    def get_Type(obj):
        return 4


class VillageSer(serializers.ModelSerializer):
    City = serializers.SerializerMethodField()

    class Meta:
        model = Village
        fields = ['Code', 'Name', 'isEconomic', 'nPopulation', 'nHousehold', 'Description', 'City', 'RegisterTime',
                  'BigVillage', 'type']
        depth = 4

    @staticmethod
    def get_City(obj):
        cityInfo = City.objects.filter(Code=obj.CityCode).first()
        return cityInfo.Name


class VillageListSer(serializers.ModelSerializer):
    Type = serializers.SerializerMethodField()

    class Meta:
        model = Village
        fields = ['Code', 'Name', 'Type']

    @staticmethod
    def get_Type(obj):
        return 5


class RedundantInformationSer(serializers.ModelSerializer):
    class Meta:
        model = RedundantInformation
        fields = ['Code', 'Name', 'ForLocation', 'isPrivate']


class ReInfoValueSer(serializers.ModelSerializer):
    class Meta:
        model = ReInformationValue
        fields = ['Code', 'RedundantInformation', 'Value']
        depth = 2


class PropertyListSer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['Code', 'Name']


class SubPropertyListSer(serializers.ModelSerializer):
    Property = serializers.SerializerMethodField()

    class Meta:
        model = SubProperty
        fields = ['Code', 'Name', 'Property']
        depth = 2

    @staticmethod
    def get_Property(obj):
        context = {
            'Code': obj.Property.Code,
            'Name': obj.Property.Name
        }
        return context


class PropertySer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyBelongPlaceSer(serializers.ModelSerializer):
    class Meta:
        model = PropertyBelongPlace
        fields = '__all__'
        depth = 2


class PropertyBelongPlaceExcelSer(serializers.ModelSerializer):
    Place = serializers.SerializerMethodField()
    Property = serializers.CharField(source='SubProperty.Property.Name', read_only=True)
    SubProperty = serializers.CharField(source='SubProperty.Name', read_only=True)
    RegisterTime = serializers.SerializerMethodField()

    class Meta:
        model = PropertyBelongPlace
        fields = ['Code', 'Property', 'SubProperty', 'Place', 'Title', 'Description', 'RegisterTime']
        depth = 2

    @staticmethod
    def get_Place(obj):
        locationInfo = BigCity.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return locationInfo.Name
        locationInfo = City.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return locationInfo.Name
        locationInfo = CityPart.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return locationInfo.Name
        locationInfo = BigVillage.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return locationInfo.Name
        locationInfo = Village.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return locationInfo.Name

    @staticmethod
    def get_RegisterTime(obj):
        return jdatetime.datetime.strftime(obj.RegisterTime, "%Y/%m/%d")


class PropertyBelongPlaceListSer(serializers.ModelSerializer):
    Place = serializers.SerializerMethodField()

    class Meta:
        model = PropertyBelongPlace
        fields = ['Code', 'SubProperty', 'Place', 'Title', 'RegisterTime', 'isPrivate']
        depth = 2

    @staticmethod
    def get_Place(obj):
        locationInfo = BigCity.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return BigCitySer(locationInfo).data
        locationInfo = City.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return CitySer(locationInfo).data
        locationInfo = CityPart.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return CityPartSer(locationInfo).data
        locationInfo = BigVillage.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return BigVillageSer(locationInfo).data
        locationInfo = Village.objects.filter(Code=obj.PlaceCode).first()
        if locationInfo:
            return VillageSer(locationInfo).data


class ProperListSer(serializers.ModelSerializer):
    class Meta:
        model = Proper
        fields = ['Code', 'Name']


class PeopleBelongLocationListSer(serializers.ModelSerializer):
    Proper = serializers.CharField(source='Proper.Name', read_only=True)

    class Meta:
        model = PeopleBelongLocation
        fields = ['Code', 'Name', 'Family', 'Proper']


class PeopleBelongLocationSer(serializers.ModelSerializer):

    class Meta:
        model = PeopleBelongLocation
        fields = ['Code', 'Name', 'Family', 'Description', 'Proper', 'AttachmentFile']
        depth = 2


class ManagerLimitDataSer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['Code', 'SirName', 'Character']
        depth = 2


class AnswerToPropertyListSer(serializers.ModelSerializer):
    Manager = serializers.SerializerMethodField()

    class Meta:
        model = AnswerToProperty
        fields = ['Code', 'Content', 'File', 'Manager', 'RegisterTime']

    @staticmethod
    def get_Manager(obj):
        managerInfo = Manager.objects.filter(Code=obj.Manager.Code).first()
        return ManagerLimitDataSer(managerInfo).data


class OrganizationSer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['Code', 'Name']


class SolutionBelongToPropertySer(serializers.ModelSerializer):
    class Meta:
        model = SolutionBelongToProperty
        fields = ['Code', 'Content', 'Organization']
        depth = 2


class AccessSectionListManagerSer(serializers.ModelSerializer):
    Code = serializers.IntegerField(source='Section.Code', read_only=True)
    Name = serializers.CharField(source='Section.Name', read_only=True)

    class Meta:
        model = AccessCharacter
        fields = ['Code', 'Name']


class SectionCodeSer(serializers.ModelSerializer):
    Code = serializers.IntegerField(source='Section.Code', read_only=True)

    class Meta:
        model = AccessCharacter
        fields = ['Code']


class CharacterSer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['Code', 'Name']


class ManagerListSer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['Code', 'Name', 'Family', 'SirName', 'NaCode', 'Phone', 'Character', 'RegisterTime']
        depth = 2


class ManagerInfoSer(serializers.ModelSerializer):
    AccessLocation = serializers.SerializerMethodField()

    class Meta:
        model = Manager
        fields = ['Code', 'Name', 'Family', 'SirName', 'NaCode', 'Phone', 'Character', 'Password', 'RegisterTime',
                  'AccessLocation']
        depth = 2

    @staticmethod
    def get_AccessLocation(obj):
        if obj.Character.AccessLevel == 3:  # responsible
            accessCodeInfo = LocationBelongToManager.objects.filter(Manager__Code=obj.Code)
            if accessCodeInfo:
                infoLocation = []
                for item in accessCodeInfo:
                    locationInfo = BigCity.objects.filter(Code=item.LocationCode).first()
                    if locationInfo:
                        infoLocation.append(BigCityListSer(locationInfo).data)
                    locationInfo = City.objects.filter(Code=item.LocationCode).first()
                    if locationInfo:
                        infoLocation.append(CityListSer(locationInfo).data)
                    locationInfo = CityPart.objects.filter(Code=item.LocationCode).first()
                    if locationInfo:
                        infoLocation.append(CityPartListSer(locationInfo).data)
                    locationInfo = BigVillage.objects.filter(Code=item.LocationCode).first()
                    if locationInfo:
                        infoLocation.append(BigVillageListSer(locationInfo).data)
                    locationInfo = Village.objects.filter(Code=item.LocationCode).first()
                    if locationInfo:
                        infoLocation.append(VillageListSer(locationInfo).data)
                return infoLocation
            else:
                return []
        else:
            return []


class AccessLocationResponsibleSer(serializers.ModelSerializer):
    Info = serializers.SerializerMethodField()

    class Meta:
        model = LocationBelongToManager
        fields = ['Info']

    @staticmethod
    def get_Info(obj):
        locationInfo = BigCity.objects.filter(Code=obj.LocationCode).first()
        if locationInfo:
            context = {
                'Code': locationInfo.Code,
                'Name': locationInfo.Name,
                'Type': locationInfo.type
            }
            return context
        locationInfo = City.objects.filter(Code=obj.LocationCode).first()
        if locationInfo:
            context = {
                'Code': locationInfo.Code,
                'Name': locationInfo.Name,
                'Type': locationInfo.type
            }
            return context
        locationInfo = CityPart.objects.filter(Code=obj.LocationCode).first()
        if locationInfo:
            context = {
                'Code': locationInfo.Code,
                'Name': locationInfo.Name,
                'Type': locationInfo.type
            }
            return context
        locationInfo = BigVillage.objects.filter(Code=obj.LocationCode).first()
        if locationInfo:
            context = {
                'Code': locationInfo.Code,
                'Name': locationInfo.Name,
                'Type': locationInfo.type
            }
            return context
        locationInfo = Village.objects.filter(Code=obj.LocationCode).first()
        if locationInfo:
            context = {
                'Code': locationInfo.Code,
                'Name': locationInfo.Name,
                'Type': locationInfo.type
            }
            return context


class SliderSer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['Code', 'Image']

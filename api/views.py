from django.shortcuts import render, reverse
from funcs.check import checkApiKey, checkInput, checkSessionKey
from rest_framework.response import Response
from rest_framework.decorators import api_view
from index.serializers import (ManagerSer, Manager, BigCity, BigCitySer, City, CitySer, CityPart, CityPartSer, \
                               BigVillage, BigVillageSer, Village, VillageSer, RedundantInformation,
                               RedundantInformationSer, ReInformationValue, CityListSer, CityPartListSer, \
                               VillageListSer, BigVillageListSer, ReInfoValueSer, BigCityListSer, Property,
                               PropertyBelongPlace, PropertySer, PropertyBelongPlaceListSer, PropertyListSer, \
                               SubProperty, SubPropertyListSer, Proper, ProperListSer, PeopleBelongLocation,
                               PeopleBelongLocationListSer, PeopleBelongLocationSer, AnswerToPropertyListSer,
                               AnswerToProperty, PropertyBelongPlaceSer, ExportPropertyList, Organization,
                               OrganizationSer, SolutionBelongToProperty, SolutionBelongToPropertySer, Section,
                               AccessSectionListManagerSer)
from index.models import AccessCharacter


# Create your views here.


def index(request):
    pass


@api_view(['POST'])
def loginCheck(request):
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    phone = request.data.get('Phone')
    password = request.data.get('Password')
    listInput = [phone, password]
    resInput = checkInput(listInput)
    if resInput is False:
        context = {
            'Status': 901,
            'Message': 'Wrong Key Input'
        }
        return Response(context)
    managerInfo = Manager.objects.filter(Phone=phone, Password=password).first()
    if managerInfo:
        managerInfoSer = ManagerSer(managerInfo).data
        context = {
            'Status': 200,
            'Manager': managerInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 400,
            'Message': 'Phone or Password is Wrong'
        }
        return Response(context)


@api_view(['POST'])
def checkSession(request):
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    session = request.data.get('Session')
    if not session:
        context = {
            'Status': 400,
            'Message': 'Session invalid'
        }
        return Response(context)
    managerInfo = Manager.objects.filter(Session=session).first()
    if managerInfo:
        managerInfoSer = ManagerSer(managerInfo).data
        context = {
            'Status': 200,
            'Manager': managerInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 400,
            'Message': 'Session invalid'
        }
        return Response(context)


@api_view(['POST'])
def getLocationListByFilter(request):
    accessCode = 7222455  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    if resManager.get('Status') == 902:
        return Response(resManager)

    phrase = request.data.get('Phrase')
    typeLocation = request.data.get('Location')
    if not typeLocation:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    listTypeLoc = [
        '1',  # Big City
        '2',  # City
        '3',  # City Part
        '4',  # Big Village
        '5',  # Village
    ]
    if typeLocation not in listTypeLoc:
        context = {
            'Status': 401,
            'Message': 'Location Value Invalid'
        }
        return Response(context)
    if typeLocation == '1':
        if phrase:
            bigCityInfo = BigCity.objects.filter(Name__contains=phrase, isDeleted=False)
        else:
            bigCityInfo = BigCity.objects.filter(isDeleted=False)
        if bigCityInfo:
            bigCityInfoSer = BigCitySer(bigCityInfo, many=True).data
            context = {
                'Status': 200,
                'Info': bigCityInfoSer
            }
            return Response(context)
        else:
            context = {
                'Status': 402,
                'Message': 'Empty List'
            }
            return Response(context)
    elif typeLocation == '2':
        if phrase:
            cityInfo = City.objects.filter(Name__contains=phrase, isDeleted=False)
        else:
            cityInfo = City.objects.filter(isDeleted=False)
        if cityInfo:
            cityInfoSer = CitySer(cityInfo, many=True).data
            context = {
                'Status': 200,
                'Info': cityInfoSer
            }
            return Response(context)
        else:
            context = {
                'Status': 402,
                'Message': 'Empty List'
            }
            return Response(context)
    elif typeLocation == '3':
        if phrase:
            cityPartInfo = CityPart.objects.filter(Name__contains=phrase, isDeleted=False)
        else:
            cityPartInfo = CityPart.objects.filter(isDeleted=False)
        if cityPartInfo:
            cityPartInfoSer = CityPartSer(cityPartInfo, many=True).data
            context = {
                'Status': 200,
                'Info': cityPartInfoSer
            }
            return Response(context)
        else:
            context = {
                'Status': 402,
                'Message': 'Empty List'
            }
            return Response(context)
    elif typeLocation == '4':
        if phrase:
            bigVillageInfo = BigVillage.objects.filter(Name__contains=phrase, isDeleted=False)
        else:
            bigVillageInfo = BigVillage.objects.filter(isDeleted=False)
        if bigVillageInfo:
            bigVillageInfoSer = BigVillageSer(bigVillageInfo, many=True).data
            context = {
                'Status': 200,
                'Info': bigVillageInfoSer
            }
            return Response(context)
        else:
            context = {
                'Status': 402,
                'Message': 'Empty List'
            }
            return Response(context)
    else:
        if phrase:
            villageInfo = Village.objects.filter(Name__contains=phrase, isDeleted=False)
        else:
            villageInfo = Village.objects.filter(isDeleted=False)
        if villageInfo:
            villageInfoSer = VillageSer(villageInfo, many=True).data
            context = {
                'Status': 200,
                'Info': villageInfoSer
            }
            return Response(context)
        else:
            context = {
                'Status': 402,
                'Message': 'Empty List'
            }
            return Response(context)


@api_view(['GET'])
def getAllRedundant(request):
    accessCode = 7681409  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    if resApi.get('Info').ForUse == 1:  # panel api key
        redundantInfo = RedundantInformation.objects.all()
    else:
        redundantInfo = RedundantInformation.objects.filter(isPrivate=False)
    if redundantInfo:
        redundantInfoSer = RedundantInformationSer(redundantInfo, many=True).data
        context = {
            'Status': 200,
            'Redundant': redundantInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Empty list'
        }
        return Response(context)


@api_view(['POST'])
def getRedundantLocation(request):
    accessCode = 7681409  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    typeLocation = request.data.get('Location')
    if not typeLocation:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if resApi.get('Info').ForUse == 1:  # panel api key
        redundantInfo = RedundantInformation.objects.filter(ForLocation=typeLocation)
    else:
        redundantInfo = RedundantInformation.objects.filter(ForLocation=typeLocation, isPrivate=False)
    if redundantInfo:
        redundantInfoSer = RedundantInformationSer(redundantInfo, many=True).data
        context = {
            'Status': 200,
            'Redundant': redundantInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 201,
            'Message': 'Empty list'
        }
        return Response(context)


@api_view(['POST'])
def addRedundantForLocation(request):
    accessCode = 7777070  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    typeLocation = request.data.get('Location')
    name = request.data.get('Name')
    isPrivate = request.data.get('isPrivate')
    if not typeLocation or not name:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    listType = [1, 2, 3, 4, 5]
    if int(typeLocation) not in listType:
        context = {
            'Status': 401,
            'Message': 'Type location invalid'
        }
        return Response(context)
    if isPrivate == 'on':
        isPrivate = True
    else:
        isPrivate = False
    RedundantInformation.objects.create(Name=name, ForLocation=typeLocation, isPrivate=isPrivate)
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def editRedundantForLocation(request):
    accessCode = 7929674  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    name = request.data.get('Name')
    isPrivate = request.data.get('isPrivate')
    if not code or not name:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    redundantInfo = RedundantInformation.objects.filter(Code=code).first()
    if not redundantInfo:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)
    redundantInfo.Name = name
    if isPrivate == 'on':
        redundantInfo.isPrivate = True
    else:
        redundantInfo.isPrivate = False
    redundantInfo.save()
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def deleteRedundantForLocation(request):
    accessCode = 7165517  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    redundantInfo = RedundantInformation.objects.filter(Code=code).first()
    if not redundantInfo:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)
    redundantValueInfo = ReInformationValue.objects.filter(RedundantInformation=redundantInfo)
    if redundantValueInfo:
        for item in redundantValueInfo:
            item.delete()
    redundantInfo.delete()
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def addPlace(request):
    accessCode = 7761892  # addPlace --> fetch from section table
    accessCodeRedundant = 7681409  # getRedundantLocation --> fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList') or accessCodeRedundant not in resManager.get('AccessList'):
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    name = request.data.get('Name')
    typeLocation = request.data.get('TypeLocation')
    nHousehold = request.data.get('nHousehold')
    nPopulation = request.data.get('nPopulation')
    typeLoc = [
        '1',  # Big City
        '2',  # City
        '3',  # City Part
        '4',  # Big Village
        '5',  # Village
    ]
    resInput = checkInput([name, typeLocation])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if typeLocation not in typeLoc:
        context = {
            'Status': 401,
            'Message': 'TypeLocation invalid'
        }
        return Response(context)
    if typeLocation == '1':  # Big City
        if not nPopulation or not nPopulation:
            context = {
                'Status': 400,
                'Message': 'Input Incomplete'
            }
            return Response(context)
        bigCityInfo = BigCity.objects.create(Name=name, nHousehold=nHousehold, nPopulation=nPopulation)
        redundantList = RedundantInformation.objects.filter(ForLocation=1)
        if redundantList:
            for item in redundantList:
                valueItem = request.data.get('{}'.format(item.Code))
                if valueItem:
                    ReInformationValue.objects.create(RedundantInformation=item, LocationCode=bigCityInfo.Code,
                                                      Value=valueItem)
        context = {
            'Status': 200
        }
        return Response(context)
    elif typeLocation == '2':  # City
        if not nPopulation or not nPopulation:
            context = {
                'Status': 400,
                'Message': 'Input Incomplete'
            }
            return Response(context)
        bigCityCode = request.data.get('BigCity')
        if not bigCityCode:
            context = {
                'Status': 400,
                'Message': 'Big City Not sent'
            }
            return Response(context)
        bigCityInfo = BigCity.objects.filter(Code=bigCityCode).first()
        if not bigCityInfo:
            context = {
                'Status': 401,
                'Message': 'big city code invalid'
            }
            return Response(context)
        cityInfo = City.objects.create(Name=name, BigCity=bigCityInfo, nHousehold=nHousehold, nPopulation=nPopulation)
        redundantList = RedundantInformation.objects.filter(ForLocation=2)
        if redundantList:
            for item in redundantList:
                valueItem = request.data.get('{}'.format(item.Code))
                if valueItem:
                    ReInformationValue.objects.create(RedundantInformation=item, LocationCode=cityInfo.Code,
                                                      Value=valueItem)
        context = {
            'Status': 200
        }
        return Response(context)
    elif typeLocation == '3':  # City Part
        bigCityCode = request.data.get('BigCity')
        if not bigCityCode:
            context = {
                'Status': 400,
                'Message': 'Big City Not sent'
            }
            return Response(context)
        bigCityInfo = BigCity.objects.filter(Code=bigCityCode).first()
        if not bigCityInfo:
            context = {
                'Status': 401,
                'Message': 'big city code invalid'
            }
            return Response(context)
        cityCode = request.data.get('City')
        if not cityCode:
            context = {
                'Status': 400,
                'Message': 'City Not sent'
            }
            return Response(context)
        cityInfo = City.objects.filter(Code=cityCode, BigCity=bigCityInfo).first()
        if not cityInfo:
            context = {
                'Status': 401,
                'Message': 'city code invalid'
            }
            return Response(context)
        cityPartInfo = CityPart.objects.create(Name=name, City=cityInfo)
        redundantList = RedundantInformation.objects.filter(ForLocation=3)
        if redundantList:
            for item in redundantList:
                valueItem = request.data.get('{}'.format(item.Code))
                if valueItem:
                    ReInformationValue.objects.create(RedundantInformation=item, LocationCode=cityPartInfo.Code,
                                                      Value=valueItem)
        context = {
            'Status': 200
        }
        return Response(context)
    elif typeLocation == '4':  # Big Village
        bigCityCode = request.data.get('BigCity')
        if not bigCityCode:
            context = {
                'Status': 400,
                'Message': 'Big City Not sent'
            }
            return Response(context)
        bigCityInfo = BigCity.objects.filter(Code=bigCityCode).first()
        if not bigCityInfo:
            context = {
                'Status': 401,
                'Message': 'big city code invalid'
            }
            return Response(context)
        cityCode = request.data.get('City')
        if not cityCode:
            context = {
                'Status': 400,
                'Message': 'City Not sent'
            }
            return Response(context)
        cityInfo = City.objects.filter(Code=cityCode, BigCity=bigCityInfo).first()
        if not cityInfo:
            context = {
                'Status': 401,
                'Message': 'city code invalid'
            }
            return Response(context)
        cityPartCode = request.data.get('CityPart')
        if not cityPartCode:
            context = {
                'Status': 400,
                'Message': 'City Part Not sent'
            }
            return Response(context)
        cityPartInfo = CityPart.objects.filter(Code=cityPartCode, City=cityInfo).first()
        if not cityPartInfo:
            context = {
                'Status': 401,
                'Message': 'city part code invalid'
            }
            return Response(context)
        bigVillageInfo = BigVillage.objects.create(Name=name, CityPart=cityPartInfo)
        redundantList = RedundantInformation.objects.filter(ForLocation=4)
        if redundantList:
            for item in redundantList:
                valueItem = request.data.get('{}'.format(item.Code))
                if valueItem:
                    ReInformationValue.objects.create(RedundantInformation=item, LocationCode=bigVillageInfo.Code,
                                                      Value=valueItem)
        context = {
            'Status': 200
        }
        return Response(context)
    else:  # village
        description = request.data.get('Description')
        isEconomic = request.data.get('isEconomic')
        resInput = checkInput([nPopulation, nHousehold, description, isEconomic])
        if not resInput:
            context = {
                'Status': 400,
                'Message': 'Input Incomplete'
            }
            return Response(context)
        bigCityCode = request.data.get('BigCity')
        if not bigCityCode:
            context = {
                'Status': 400,
                'Message': 'Big City Not sent'
            }
            return Response(context)
        bigCityInfo = BigCity.objects.filter(Code=bigCityCode).first()
        if not bigCityInfo:
            context = {
                'Status': 401,
                'Message': 'big city code invalid'
            }
            return Response(context)
        cityCode = request.data.get('City')
        if not cityCode:
            context = {
                'Status': 400,
                'Message': 'City Not sent'
            }
            return Response(context)
        cityInfo = City.objects.filter(Code=cityCode, BigCity=bigCityInfo).first()
        if not cityInfo:
            context = {
                'Status': 401,
                'Message': 'city code invalid'
            }
            return Response(context)
        cityPartCode = request.data.get('CityPart')
        if not cityPartCode:
            context = {
                'Status': 400,
                'Message': 'City Part Not sent'
            }
            return Response(context)
        cityPartInfo = CityPart.objects.filter(Code=cityPartCode, City=cityInfo).first()
        if not cityPartInfo:
            context = {
                'Status': 401,
                'Message': 'city part code invalid'
            }
            return Response(context)
        bigVillageCode = request.data.get('BigVillage')
        if not bigVillageCode:
            context = {
                'Status': 400,
                'Message': 'Big Village Not sent'
            }
            return Response(context)
        bigVillageInfo = BigVillage.objects.filter(Code=bigVillageCode, CityPart=cityPartInfo).first()
        if not bigVillageInfo:
            context = {
                'Status': 401,
                'Message': 'big village code invalid'
            }
            return Response(context)
        villageInfo = Village.objects.create(Name=name, CityCode=cityCode, nHousehold=nHousehold,
                                             BigVillage=bigVillageInfo, nPopulation=nPopulation,
                                             Description=description, isEconomic=isEconomic)
        redundantList = RedundantInformation.objects.filter(ForLocation=5)
        if redundantList:
            for item in redundantList:
                valueItem = request.data.get('{}'.format(item.Code))
                if valueItem:
                    ReInformationValue.objects.create(RedundantInformation=item, LocationCode=villageInfo.Code,
                                                      Value=valueItem)
        context = {
            'Status': 200
        }
        return Response(context)


@api_view(['GET'])
def getBigCityList(request):
    accessCode = 7846799  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    bigCityInfo = BigCity.objects.filter(isDeleted=False)
    if bigCityInfo:
        bigCityInfoSer = BigCityListSer(bigCityInfo, many=True).data
        context = {
            'Status': 200,
            'List': bigCityInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'empty list'
        }
        return Response(context)


@api_view(['POST'])
def getCityList(request):
    accessCode = 7846799  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    code = request.data.get('Code')  # big city code
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    cityInfo = City.objects.filter(BigCity__Code=code, isDeleted=False)
    if cityInfo:
        cityInfoSer = CityListSer(cityInfo, many=True).data
        context = {
            'Status': 200,
            'List': cityInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code not found or empty list'
        }
        return Response(context)


@api_view(['POST'])
def getCityPartList(request):
    accessCode = 7846799  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    cityCode = request.data.get('Code')  # city code
    if not cityCode:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    cityPartInfo = CityPart.objects.filter(City__Code=cityCode, isDeleted=False)
    if cityPartInfo:
        cityPartInfoSer = CityPartListSer(cityPartInfo, many=True).data
        context = {
            'Status': 200,
            'List': cityPartInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'City Part not found'
        }
        return Response(context)


@api_view(['POST'])
def getBigVillageList(request):
    accessCode = 7846799  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    cityPartCode = request.data.get('Code')  # city part code
    if not cityPartCode:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    bigVillage = BigVillage.objects.filter(CityPart__Code=cityPartCode, isDeleted=False)
    if bigVillage:
        bigVillageSer = BigVillageListSer(bigVillage, many=True).data
        context = {
            'Status': 200,
            'List': bigVillageSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'City Part not found'
        }
        return Response(context)


@api_view(['POST'])
def getVillageList(request):
    accessCode = 7846799  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    bigVillageCode = request.data.get('Code')  # big village code
    if not bigVillageCode:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    villageInfo = Village.objects.filter(BigVillage__Code=bigVillageCode, isDeleted=False)
    if villageInfo:
        villageInfoSer = VillageListSer(villageInfo, many=True).data
        context = {
            'Status': 200,
            'List': villageInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'City Part not found'
        }
        return Response(context)


@api_view(['POST'])
def deletePlace(request):
    accessCode = 7742149  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if type(code) is not list:
        context = {
            'Status': 402,
            'Message': 'send list of code'
        }
        return Response(context)
    for item in code:
        if str(item).startswith('5'):  # Code
            cityInfo = City.objects.filter(Code=item).first()
            bigCityInfo = BigCity.objects.filter(Code=item).first()
            if cityInfo:
                cityInfo.isDeleted = True
                cityInfo.save()
            elif bigCityInfo:
                bigCityInfo.isDeleted = True
                bigCityInfo.save()
            else:
                context = {
                    'Status': 401,
                    'Message': 'Code invalid'
                }
                return Response(context)
        elif str(item).startswith('2'):  # village
            villageInfo = Village.objects.filter(Code=item).first()
            if villageInfo:
                villageInfo.isDeleted = True
                villageInfo.save()
            else:
                context = {
                    'Status': 401,
                    'Message': 'Code invalid'
                }
                return Response(context)
        else:  # other
            bigVillageInfo = BigVillage.objects.filter(Code=item).first()
            if bigVillageInfo:
                bigVillageInfo.isDeleted = True
                bigVillageInfo.save()
            cityPartInfo = CityPart.objects.filter(Code=item).first()
            if cityPartInfo:
                cityPartInfo.isDeleted = True
                cityPartInfo.save()
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def editPlace(request):
    accessCode = 7386248  # editPlace --> fetch from section table
    accessCodeRedundant = 7681409  # getRedundantLocation --> fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    name = request.data.get('Name')
    nHousehold = request.data.get('nHousehold')
    nPopulation = request.data.get('nPopulation')
    resInput = checkInput([code, name])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    villageInfo = Village.objects.filter(Code=code).first()
    bigCityInfo = BigCity.objects.filter(Code=code).first()
    bigVillageInfo = BigVillage.objects.filter(Code=code).first()
    cityPartInfo = CityPart.objects.filter(Code=code).first()
    cityInfo = City.objects.filter(Code=code).first()
    placeInfo = None
    listInfo = [villageInfo, bigVillageInfo, bigCityInfo, cityInfo, cityPartInfo]
    for item in listInfo:
        if item:
            placeInfo = item
            break
    if placeInfo is None:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)
    if not nPopulation or not nHousehold:
        context = {
            'Status': 402,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    redundantList = RedundantInformation.objects.filter(ForLocation=placeInfo.type)
    if redundantList:
        for item in redundantList:
            valueItem = request.data.get('{}'.format(item.Code))
            if valueItem:
                reInfoValue = ReInformationValue.objects.filter(RedundantInformation=item,
                                                                LocationCode=placeInfo.Code).first()
                if reInfoValue:
                    reInfoValue.Value = valueItem
                    reInfoValue.save()
                else:
                    ReInformationValue.objects.create(RedundantInformation=item, LocationCode=placeInfo.Code,
                                                      Value=valueItem)

    if placeInfo.type == 5:  # village
        isEconomic = request.data.get('isEconomic')
        description = request.data.get('Description')
        if not isEconomic or not description:
            context = {
                'Status': 402,
                'Message': 'Input Incomplete'
            }
            return Response(context)
        placeInfo.isEconomic = isEconomic
        placeInfo.Description = description
    placeInfo.nPopulation = nPopulation
    placeInfo.nHousehold = nHousehold
    placeInfo.Name = name
    placeInfo.save()
    context = {
        'Status': 200,
    }
    return Response(context)


@api_view(['POST'])
def getInfoPlace(request):
    accessCode = 7230963  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if str(code).startswith('5'):  # Code
        cityInfo = City.objects.filter(Code=code).first()
        bigCityInfo = BigCity.objects.filter(Code=code).first()
        if cityInfo:
            context = {
                'Status': 200,
                'Info': CitySer(cityInfo).data,
                'RedundantList': None,
                'RedundantInfo': None
            }
            if resApi.get('Info').ForUse == 1:  # panel api key
                redundantInfo = RedundantInformation.objects.filter(ForLocation=2)
            else:
                redundantInfo = RedundantInformation.objects.filter(ForLocation=2, isPrivate=False)
            if redundantInfo:
                context['RedundantList'] = RedundantInformationSer(redundantInfo, many=True).data
                reInfoValue = ReInformationValue.objects.filter(LocationCode=cityInfo.Code)
                if reInfoValue:
                    context['RedundantInfo'] = ReInfoValueSer(reInfoValue, many=True).data
            return Response(context)
        elif bigCityInfo:
            context = {
                'Status': 200,
                'Info': BigCitySer(bigCityInfo).data,
                'RedundantList': None,
                'RedundantInfo': None
            }
            if resApi.get('Info').ForUse == 1:  # panel api key
                redundantInfo = RedundantInformation.objects.filter(ForLocation=1)
            else:
                redundantInfo = RedundantInformation.objects.filter(ForLocation=1, isPrivate=False)
            if redundantInfo:
                context['RedundantList'] = RedundantInformationSer(redundantInfo, many=True).data
                reInfoValue = ReInformationValue.objects.filter(LocationCode=bigCityInfo.Code)
                if reInfoValue:
                    context['RedundantInfo'] = ReInfoValueSer(reInfoValue, many=True).data
            return Response(context)
        else:
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    elif str(code).startswith('2'):  # village
        villageInfo = Village.objects.filter(Code=code).first()
        if villageInfo:
            context = {
                'Status': 200,
                'Info': VillageSer(villageInfo).data,
                'RedundantList': None,
                'RedundantInfo': None
            }
            if resApi.get('Info').ForUse == 1:  # panel api key
                redundantInfo = RedundantInformation.objects.filter(ForLocation=5)
            else:
                redundantInfo = RedundantInformation.objects.filter(ForLocation=5, isPrivate=False)
            if redundantInfo:
                context['RedundantList'] = RedundantInformationSer(redundantInfo, many=True).data
                reInfoValue = ReInformationValue.objects.filter(LocationCode=villageInfo.Code)
                if reInfoValue:
                    context['RedundantInfo'] = ReInfoValueSer(reInfoValue, many=True).data
        else:
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    else:  # other
        bigVillageInfo = BigVillage.objects.filter(Code=code).first()
        if bigVillageInfo:
            context = {
                'Status': 200,
                'Info': BigVillageSer(bigVillageInfo).data,
                'RedundantList': None,
                'RedundantInfo': None
            }
            if resApi.get('Info').ForUse == 1:  # panel api key
                redundantInfo = RedundantInformation.objects.filter(ForLocation=4)
            else:
                redundantInfo = RedundantInformation.objects.filter(ForLocation=4, isPrivate=False)
            if redundantInfo:
                context['RedundantList'] = RedundantInformationSer(redundantInfo, many=True).data
                reInfoValue = ReInformationValue.objects.filter(LocationCode=bigVillageInfo.Code)
                if reInfoValue:
                    context['RedundantInfo'] = ReInfoValueSer(reInfoValue, many=True).data
            return Response(context)
        cityPartInfo = CityPart.objects.filter(Code=code).first()
        if cityPartInfo:
            context = {
                'Status': 200,
                'Info': CityPartSer(cityPartInfo).data,
                'RedundantList': None,
                'RedundantInfo': None
            }
            if resApi.get('Info').ForUse == 1:  # panel api key
                redundantInfo = RedundantInformation.objects.filter(ForLocation=3)
            else:
                redundantInfo = RedundantInformation.objects.filter(ForLocation=3, isPrivate=False)
            if redundantInfo:
                context['RedundantList'] = RedundantInformationSer(redundantInfo, many=True).data
                reInfoValue = ReInformationValue.objects.filter(LocationCode=cityPartInfo.Code)
                if reInfoValue:
                    context['RedundantInfo'] = ReInfoValueSer(reInfoValue, many=True).data
            return Response(context)
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['POST'])
def getPropertyListByFilter(request):
    accessCode = 7738915  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    phrase = request.data.get('Phrase')
    typeLocation = request.data.get('TypeLocation')
    if not typeLocation:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    try:
        typeLocation = int(typeLocation)
    except Exception as e:
        context = {
            "Status": 401,
            'Message': 'type location invalid',
            'Error': e.__class__.__name__
        }
        return Response(context)
    listType = [1, 2, 3, 4, 5]
    if typeLocation not in listType:
        context = {
            'Status': 401,
            'Message': 'type location invalid'
        }
        return Response(context)
    if typeLocation == 1:  # big city
        locationInfo = BigCity.objects.filter(isDeleted=False)
    elif typeLocation == 2:  # city
        locationInfo = City.objects.filter(isDeleted=False)
    elif typeLocation == 3:  # city part
        locationInfo = CityPart.objects.filter(isDeleted=False)
    elif typeLocation == 4:  # big village
        locationInfo = BigVillage.objects.filter(isDeleted=False)
    else:
        locationInfo = Village.objects.filter(isDeleted=False)
    if locationInfo:
        listCode = []
        for item in locationInfo:
            listCode.append(item.Code)
        if phrase:
            if resApi.get('Info').ForUse == 1:  # panel api key
                propertyInfo = PropertyBelongPlace.objects.filter(PlaceCode__in=listCode, Title__contains=phrase)
            else:
                propertyInfo = PropertyBelongPlace.objects.filter(PlaceCode__in=listCode, Title__contains=phrase,
                                                                  isPrivate=False)
        else:
            if resApi.get('Info').ForUse == 1:  # panel api key
                propertyInfo = PropertyBelongPlace.objects.filter(PlaceCode__in=listCode)
            else:
                propertyInfo = PropertyBelongPlace.objects.filter(PlaceCode__in=listCode, isPrivate=False)
        if propertyInfo:
            propertyInfoSer = PropertyBelongPlaceListSer(propertyInfo, many=True).data
            context = {
                'Status': 200,
                'Property': propertyInfoSer
            }
            return Response(context)
        else:
            context = {
                'Status': 201,
                'Message': 'Empty List'
            }
            return Response(context)
    else:
        context = {
            'Status': 201,
            'Message': 'Empty List'
        }
        return Response(context)


@api_view(['POST'])
def getInfoPropertyBToPlace(request):
    accessCode = 7564621  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if resApi.get('Info').ForUse == 1:  # panel api key
        propertyInfo = PropertyBelongPlace.objects.filter(Code=code).first()
    else:
        propertyInfo = PropertyBelongPlace.objects.filter(Code=code, isPrivate=False).first()
    if propertyInfo:
        propertyInfoSer = PropertyBelongPlaceSer(propertyInfo).data
        context = {
            'Status': 200,
            'Property': propertyInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid or Access denied'
        }
        return Response(context)


@api_view(['POST'])
def deletePropertyBelongToPlace(request):
    accessCode = 7818334  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if type(code) is not list:
        context = {
            'Status': 401,
            'Message': 'send list'
        }
        return Response(context)
    for item in code:
        propertyInfo = PropertyBelongPlace.objects.filter(Code=item).first()
        if propertyInfo:
            propertyInfo.delete()
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['GET'])
def getPropertyNameList(request):
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
    propertyInfo = Property.objects.all()
    if propertyInfo:
        propertyInfoSer = PropertyListSer(propertyInfo, many=True).data
        context = {
            'Status': 200,
            'Property': propertyInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 400,
            'Message': 'Empty List'
        }
        return Response(context)


@api_view(['POST'])
def getSubPropertyNameList(request):
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    subPropertyInfo = SubProperty.objects.filter(Property__Code=code)
    if subPropertyInfo:
        subPropertyInfoSer = SubPropertyListSer(subPropertyInfo, many=True).data
        context = {
            'Status': 200,
            'SubProperty': subPropertyInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Empty List'
        }
        return Response(context)


@api_view(['GET'])
def getAllSubPropertyNameList(request):
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
    subPropertyInfo = SubProperty.objects.all()
    if subPropertyInfo:
        subPropertyInfoSer = SubPropertyListSer(subPropertyInfo, many=True).data
        context = {
            'Status': 200,
            'SubProperty': subPropertyInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Empty List'
        }
        return Response(context)


@api_view(['POST'])
def addPropertyToPlace(request):
    accessCode = 7478868  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    placeCode = request.data.get('LocationCode')
    typeLocation = request.data.get('TypeLocation')
    subProperty = request.data.get('SubProperty')
    title = request.data.get('Title')
    description = request.data.get('Description')
    isPrivate = request.data.get('isPrivate')
    image = request.FILES.get('Image')
    resInput = checkInput([placeCode, typeLocation, subProperty, title, description])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if not typeLocation:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    try:
        typeLocation = int(typeLocation)
    except Exception as e:
        context = {
            "Status": 401,
            'Message': 'type location invalid',
            'Error': e.__class__.__name__
        }
        return Response(context)
    listType = [1, 2, 3, 4, 5]
    if typeLocation not in listType:
        context = {
            'Status': 401,
            'Message': 'type location invalid'
        }
        return Response(context)
    if typeLocation == 1:  # big city
        locationInfo = BigCity.objects.filter(Code=placeCode).first()
    elif typeLocation == 2:  # city
        locationInfo = City.objects.filter(Code=placeCode).first()
    elif typeLocation == 3:  # city part
        locationInfo = CityPart.objects.filter(Code=placeCode).first()
    elif typeLocation == 4:  # big village
        locationInfo = BigVillage.objects.filter(Code=placeCode).first()
    else:
        locationInfo = Village.objects.filter(Code=placeCode).first()
    if not locationInfo:
        context = {
            'Status': 402,
            'Message': 'Location code invalid'
        }
        return Response(context)
    subPropertyInfo = SubProperty.objects.filter(Code=subProperty).first()
    if not subPropertyInfo:
        context = {
            'Status': 403,
            'Message': 'SubProperty code invalid'
        }
        return Response(context)
    if isPrivate == 'on':
        isPrivate = True
    else:
        isPrivate = False
    if image:
        propertyInfo = PropertyBelongPlace.objects.create(PlaceCode=placeCode, SubProperty=subPropertyInfo, Title=title,
                                                          Description=description, Image=image, isPrivate=isPrivate)
    else:
        propertyInfo = PropertyBelongPlace.objects.create(PlaceCode=placeCode, SubProperty=subPropertyInfo, Title=title,
                                                          Description=description, isPrivate=isPrivate)
    context = {
        'Status': 200,
        'Code': propertyInfo.Code
    }
    return Response(context)


@api_view(['POST'])
def editPropertyToPlace(request):
    accessCode = 7346060  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    title = request.data.get('Title')
    description = request.data.get('Description')
    isPrivate = request.data.get('isPrivate')
    image = request.FILES.get('Image')
    resInput = checkInput([code, title, description])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    propertyInfo = PropertyBelongPlace.objects.filter(Code=code).first()
    if propertyInfo:
        propertyInfo.Title = title
        propertyInfo.Description = description
        if image:
            propertyInfo.Image = image
        if isPrivate == 'on':
            propertyInfo.isPrivate = True
        else:
            propertyInfo.isPrivate = False
        propertyInfo.save()
        context = {
            'Status': 200
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['GET'])
def getProperList(request):
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
    properInfo = Proper.objects.all()
    if properInfo:
        properInfoSer = ProperListSer(properInfo, many=True).data
        context = {
            'Status': 200,
            'Proper': properInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 201,
            'Message': 'Empty list'
        }
        return Response(context)


@api_view(['POST'])
def getPeopleBelongToPlaceList(request):
    accessCode = 7213024  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if resApi.get('Info').ForUse == 1:  # panel api key
        peopleInfo = PeopleBelongLocation.objects.filter(LocationCode=code)
    else:
        peopleInfo = PeopleBelongLocation.objects.filter(LocationCode=code, isPrivate=False)
    if peopleInfo:
        peopleInfoSer = PeopleBelongLocationListSer(peopleInfo, many=True).data
        context = {
            'Status': 200,
            'People': peopleInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 201,
            'Message': 'empty list'
        }
        return Response(context)


@api_view(['POST'])
def getInfoPeopleBelongToPlace(request):
    accessCode = 7194645  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if resApi.get('Info').ForUse == 1:  # panel api key
        peopleInfo = PeopleBelongLocation.objects.filter(Code=code).first()
    else:
        peopleInfo = PeopleBelongLocation.objects.filter(Code=code, isPrivate=False).first()
    if peopleInfo:
        peopleInfoSer = PeopleBelongLocationSer(peopleInfo).data
        context = {
            'Status': 200,
            'People': peopleInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid or Access denied'
        }
        return Response(context)


@api_view(['POST'])
def addPeopleBelongToPlace(request):
    accessCode = 7656661  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    locationCode = request.data.get('Code')
    proper = request.data.get('Proper')
    name = request.data.get('Name')
    family = request.data.get('Family')
    description = request.data.get('Description')
    attachFile = request.FILES.get('AttachFile')
    resInput = checkInput([locationCode, proper, name, family, description])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    locationInfo = None
    if str(locationCode).startswith('5'):  # Code
        cityInfo = City.objects.filter(Code=locationCode).first()
        bigCityInfo = BigCity.objects.filter(Code=locationCode).first()
        if cityInfo:
            locationInfo = cityInfo
        elif bigCityInfo:
            locationInfo = bigCityInfo
        else:
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    elif str(locationCode).startswith('2'):  # village
        villageInfo = Village.objects.filter(Code=locationCode).first()
        if villageInfo:
            locationInfo = villageInfo
        else:
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    else:  # other
        bigVillageInfo = BigVillage.objects.filter(Code=locationCode).first()
        cityPartInfo = CityPart.objects.filter(Code=locationCode).first()
        if bigVillageInfo:
            locationInfo = bigVillageInfo
        elif cityPartInfo:
            locationInfo = cityPartInfo
        else:
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    if locationInfo is None:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)
    properInfo = Proper.objects.filter(Code=proper).first()
    if not properInfo:
        context = {
            'Status': 402,
            'Message': 'Proper invalid'
        }
        return Response(context)
    if attachFile:
        PeopleBelongLocation.objects.create(Name=name, Family=family, LocationCode=locationCode, Proper=properInfo,
                                            Description=description, AttachmentFile=attachFile)
    else:
        PeopleBelongLocation.objects.create(Name=name, Family=family, LocationCode=locationCode, Proper=properInfo,
                                            Description=description)
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def editPeopleBelongToPlace(request):
    accessCode = 7222915  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    proper = request.data.get('Proper')
    name = request.data.get('Name')
    family = request.data.get('Family')
    description = request.data.get('Description')
    attachFile = request.FILES.get('AttachFile')
    resInput = checkInput([code, proper, name, family, description])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    properInfo = Proper.objects.filter(Code=proper).first()
    if not properInfo:
        context = {
            'Status': 402,
            'Message': 'Proper invalid'
        }
        return Response(context)
    peopleInfo = PeopleBelongLocation.objects.filter(Code=code).first()
    if peopleInfo:
        peopleInfo.Proper = properInfo
        peopleInfo.Name = name
        peopleInfo.Family = family
        peopleInfo.Description = description
        if peopleInfo:
            peopleInfo.AttachmentFile = attachFile
        peopleInfo.save()
        context = {
            'Status': 200
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['POST'])
def deletePeopleBelongToPlace(request):
    accessCode = 7178311  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    peopleInfo = PeopleBelongLocation.objects.filter(Code=code).first()
    if peopleInfo:
        peopleInfo.delete()
        context = {
            'Status': 200
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['POST'])
def addSubProperty(request):
    accessCode = 7282395  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    name = request.data.get('Name')
    propertyCode = request.data.get('Property')
    if not name or not propertyCode:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    propertyInfo = Property.objects.filter(Code=propertyCode).first()
    if not propertyInfo:
        context = {
            'Status': 401,
            'Message': 'Property invalid'
        }
        return Response(context)
    SubProperty.objects.create(Name=name, Property=propertyInfo)
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def editSubProperty(request):
    accessCode = 7461457  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    name = request.data.get('Name')
    propertyCode = request.data.get('Property')
    resInput = checkInput([code, name, propertyCode])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    propertyInfo = Property.objects.filter(Code=propertyCode).first()
    if not propertyInfo:
        context = {
            'Status': 401,
            'Message': 'Property invalid'
        }
        return Response(context)
    subPropertyInfo = SubProperty.objects.filter(Code=code).first()
    if subPropertyInfo:
        subPropertyInfo.Name = name
        subPropertyInfo.Property = propertyInfo
        subPropertyInfo.save()
        context = {
            'Status': 200
        }
        return Response(context)
    else:
        context = {
            'Status': 402,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['POST'])
def deleteSubProperty(request):
    accessCode = 7927037  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    subPropertyInfo = SubProperty.objects.filter(Code=code).first()
    if subPropertyInfo:
        propertyBelongToPlaceInfo = PropertyBelongPlace.objects.filter(SubProperty=subPropertyInfo)
        if propertyBelongToPlaceInfo:
            for item in propertyBelongToPlaceInfo:
                item.delete()
        subPropertyInfo.delete()
        context = {
            'Status': 200,
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['POST'])
def getAnswerPropertyBToPlaceList(request):
    accessCode = 7437982  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    if resApi.get('Info').ForUse == 1:  # panel api key
        answerInfo = AnswerToProperty.objects.filter(PropertyBelongPlace__Code=code).order_by('RegisterTime')
    else:
        answerInfo = AnswerToProperty.objects.filter(PropertyBelongPlace__Code=code,
                                                     PropertyBelongPlace__isPrivate=False).order_by('RegisterTime')
    if answerInfo:
        answerInfoSer = AnswerToPropertyListSer(answerInfo, many=True).data
        context = {
            'Status': 200,
            'Answer': answerInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid or Access denied'
        }
        return Response(context)


@api_view(['POST'])
def addAnswerToProperty(request):
    accessCode = 7989918  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    propertyPlaceCode = request.data.get('PropertyPlaceCode')
    content = request.data.get('Content')
    file = request.FILES.get('File')
    resInput = checkInput([propertyPlaceCode, content])
    if not resInput:
        context = {
            "Status": 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    propertyInfo = PropertyBelongPlace.objects.filter(Code=propertyPlaceCode).first()
    if not propertyInfo:
        context = {
            'Status': 401,
            'Message': 'PropertyPlaceCode invalid'
        }
        return Response(context)
    if file:
        AnswerToProperty.objects.create(PropertyBelongPlace=propertyInfo, Manager=resManager.get('Manager'),
                                        Content=content, File=file)
    else:
        AnswerToProperty.objects.create(PropertyBelongPlace=propertyInfo, Manager=resManager.get('Manager'),
                                        Content=content)
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def editAnswerProperty(request):
    accessCode = 7567638  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    content = request.data.get('Content')
    file = request.FILES.get('File')
    resInput = checkInput([code, content])
    if not resInput:
        context = {
            "Status": 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    answerInfo = AnswerToProperty.objects.filter(Code=code, Manager=resManager.get('Manager')).first()
    if answerInfo:
        # answerInfo.RegisterTime = jdatetime.datetime.today()
        answerInfo.Content = content
        if file:
            answerInfo.File = file
        answerInfo.save()
        context = {
            'Status': 200
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['POST'])
def deleteAnswerProperty(request):
    accessCode = 7317685  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            "Status": 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    answerInfo = AnswerToProperty.objects.filter(Code=code, Manager=resManager.get('Manager')).first()
    if answerInfo:
        answerInfo.delete()
        context = {
            'Status': 200
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['POST'])
def getFullInfoPropertyBToPlace(request):
    accessCode = 7990572  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input Incomplete'
        }
        return Response(context)
    locationInfo = None
    if str(code).startswith('5'):  # Code
        cityInfo = City.objects.filter(Code=code).first()
        bigCityInfo = BigCity.objects.filter(Code=code).first()
        if cityInfo:
            locationInfo = cityInfo
        elif bigCityInfo:
            locationInfo = bigCityInfo
        else:
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    elif str(code).startswith('2'):  # village
        villageInfo = Village.objects.filter(Code=code).first()
        if villageInfo:
            locationInfo = villageInfo
        else:
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    else:  # other
        bigVillageInfo = BigVillage.objects.filter(Code=code).first()
        cityPartInfo = CityPart.objects.filter(Code=code).first()
        if bigVillageInfo:
            locationInfo = bigVillageInfo
        elif cityPartInfo:
            locationInfo = cityPartInfo
        else:
            context = {
                'Status': 401,
                'Message': 'Code invalid'
            }
            return Response(context)
    if locationInfo is None:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)
    propertyBToPlaceInfo = PropertyBelongPlace.objects.filter(PlaceCode=locationInfo.Code)
    if propertyBToPlaceInfo:
        propertyInfo = Property.objects.all()
        info = []
        for item in propertyInfo:
            inf = propertyBToPlaceInfo.filter(SubProperty__Property__Code=item.Code)
            if inf:
                prop = PropertyBelongPlaceSer(inf, many=True).data
            else:
                prop = None
            dic = {
                'Info': RedundantInformationSer(item).data,
                'PropertyBelongToPlace': prop
            }
            info.append(dic)
        context = {
            'Status': 200,
            'Property': info,
        }
        return Response(context)
    else:
        context = {
            'Status': 201,
            'Message': 'Empty list'
        }
        return Response(context)


@api_view(['POST'])
def getUrlExportPropertyToExcel(request):
    accessCode = 7981699  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input incomplete'
        }
        return Response(context)
    if type(code) is not list:
        context = {
            'Status': 401,
            'Message': 'send list'
        }
        return Response(context)
    saveList = ExportPropertyList.objects.create(List=str(code))
    context = {
        'Status': 200,
        'Link': '{}'.format(reverse('index-exportPropertyToExcel', kwargs={'code': saveList.Code}))
    }
    return Response(context)


@api_view(['GET'])
def getAllOrganization(request):
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
    orgInfo = Organization.objects.all()
    if orgInfo:
        orgInfoSer = OrganizationSer(orgInfo, many=True).data
        context = {
            'Status': 200,
            'Organization': orgInfoSer
        }
        return Response(context)
    else:
        context = {
            'Status': 201,
            'Message': 'Empty list'
        }
        return Response(context)


@api_view(['POST'])
def getSolutionToProperty(request):
    accessCode = 7185888  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 1:  # panel api key
        session = request.headers.get('Session')
        resManager = checkSessionKey(session)
        if resManager.get('Status') == 902:
            return Response(resManager)
        if accessCode not in resManager.get('AccessList'):  # access denied
            context = {
                'Status': -1,
                'Message': 'Access Denied'
            }
            return Response(context)
    code = request.data.get('Code')  # property Code
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input incomplete'
        }
        return Response(context)
    if resApi.get('Info').ForUse == 1:  # panel api key
        propertyInfo = PropertyBelongPlace.objects.filter(Code=code).first()
    else:
        propertyInfo = PropertyBelongPlace.objects.filter(Code=code, isPrivate=False).first()
    if propertyInfo:
        solutionInfo = SolutionBelongToProperty.objects.filter(PropertyBelongPlace=propertyInfo)
        if solutionInfo:
            solutionInfoSer = SolutionBelongToPropertySer(solutionInfo, many=True).data
            context = {
                'Status': 200,
                'Solution': solutionInfoSer
            }
            return Response(context)
        else:
            context = {
                'Status': 201,
                'Message': 'Empty list'
            }
            return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid or Access denied'
        }
        return Response(context)


@api_view(['POST'])
def addSolutionToProperty(request):
    accessCode = 7387548  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')  # property Code
    content = request.data.get('Content')
    organization = request.data.get('Organization')
    resInput = checkInput([code, content, organization])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input incomplete'
        }
        return Response(context)
    orgInfo = Organization.objects.filter(Code=organization).first()
    if not orgInfo:
        context = {
            'Status': 401,
            'Message': 'Organization invalid'
        }
        return Response(context)
    propertyInfo = PropertyBelongPlace.objects.filter(Code=code).first()
    if not propertyInfo:
        context = {
            'Status': 402,
            'Message': 'Property Code invalid'
        }
        return Response(context)
    SolutionBelongToProperty.objects.create(Content=content, Organization=orgInfo, PropertyBelongPlace=propertyInfo)
    context = {
        'Status': 200
    }
    return Response(context)


@api_view(['POST'])
def editSolutionToProperty(request):
    accessCode = 7175319  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    content = request.data.get('Content')
    organization = request.data.get('Organization')
    resInput = checkInput([code, content, organization])
    if not resInput:
        context = {
            'Status': 400,
            'Message': 'Input incomplete'
        }
        return Response(context)
    orgInfo = Organization.objects.filter(Code=organization).first()
    if not orgInfo:
        context = {
            'Status': 401,
            'Message': 'Organization invalid'
        }
        return Response(context)
    solutionInfo = SolutionBelongToProperty.objects.filter(Code=code).first()
    if solutionInfo:
        solutionInfo.Content = content
        solutionInfo.Organization = orgInfo
        solutionInfo.save()
        context = {
            'Status': 200
        }
        return Response(context)
    else:
        context = {
            'Status': 402,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['POST'])
def deleteSolutionToProperty(request):
    accessCode = 7276026  # fetch from section table
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    if accessCode not in resManager.get('AccessList'):  # access denied
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    code = request.data.get('Code')
    if not code:
        context = {
            'Status': 400,
            'Message': 'Input incomplete'
        }
        return Response(context)
    solutionInfo = SolutionBelongToProperty.objects.filter(Code=code).first()
    if solutionInfo:
        solutionInfo.delete()
        context = {
            'Status': 200
        }
        return Response(context)
    else:
        context = {
            'Status': 401,
            'Message': 'Code invalid'
        }
        return Response(context)


@api_view(['GET'])
def getAccessListManager(request):
    apiKey = request.headers.get('API-X-KEY')
    resApi = checkApiKey(apiKey)
    if resApi.get('Status') == 900:
        return Response(resApi)
    if resApi.get('Info').ForUse == 2:  # blog api key
        context = {
            'Status': -1,
            'Message': 'Access Denied'
        }
        return Response(context)
    session = request.headers.get('Session')
    resManager = checkSessionKey(session)
    if resManager.get('Status') == 902:
        return Response(resManager)
    accessCharacterInfo = AccessCharacter.objects.filter(Character=resManager.get('Manager').Character)
    if accessCharacterInfo:
        accessListSer = AccessSectionListManagerSer(accessCharacterInfo, many=True).data
        context = {
            'Status': 200,
            'AccessList': accessListSer
        }
        return Response(context)
    else:
        context = {
            'Status': 201,
            'Message': 'Empty list'
        }
        return Response(context)

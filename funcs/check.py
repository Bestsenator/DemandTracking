from index.models import APIKEY, Manager, AccessCharacter, LocationBelongToManager
from index.serializers import SectionCodeSer
import re


def checkApiKey(key):
    if not key:
        context = {
            'Status': 900,  # api key not sent
            'Message': 'Api Key is not sent'
        }
        return context
    apiInfo = APIKEY.objects.filter(ApiKey=key).first()
    if not apiInfo:
        context = {
            'Status': 900,  # api key invalid
            'Message': 'Api Key invalid'
        }
        return context
    context = {
        'Status': 200,  # api key invalid
        'Info': apiInfo
    }
    return context


def checkSessionKey(key):
    if not key:
        context = {
            'Status': 902,  # session not sent
            'Message': 'Session is not sent'
        }
        return context
    managerInfo = Manager.objects.filter(Session=key).first()
    if not managerInfo:
        context = {
            'Status': 902,  # session invalid
            'Message': 'Session invalid'
        }
        return context
    accessCodeInfo = AccessCharacter.objects.filter(Character=managerInfo.Character)
    if accessCodeInfo:
        accessCodeInfoSer = []
        accessCodeInfoSerWithDict = SectionCodeSer(accessCodeInfo, many=True).data
        for item in accessCodeInfoSerWithDict:
            accessCodeInfoSer.append(item.get('Code'))
    else:
        accessCodeInfoSer = []
    context = {
        'Status': 200,
        'Manager': managerInfo,
        'AccessList': accessCodeInfoSer
    }
    if managerInfo.Character.AccessLevel == 3:  # responsible
        locationInfo = LocationBelongToManager.objects.filter(Manager=managerInfo)
        listLoc = []
        if locationInfo:
            for item in locationInfo:
                listLoc.append(item.LocationCode)
        context['AccessLocation'] = listLoc
    return context


def checkInput(inputs):
    for i in inputs:
        if not i and i != 0:
            return False
    return True


def checkPhone(phone, tp):
    if tp == 'phone':
        if not phone.startswith('09'):
            return False
    if tp == 'line':
        if not phone.startswith('0'):
            return False
    if len(phone) != 11:
        return False
    return True


def checkPassword(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

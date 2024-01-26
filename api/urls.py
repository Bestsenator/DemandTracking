from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='api-index'),
    path('loginCheck/', views.loginCheck, name='api-loginCheck'),
    path('checkSession/', views.checkSession, name='api-checkSession'),
    path('getLocationListByFilter/', views.getLocationListByFilter, name='api-getLocationListByFilter'),
    path('getRedundantLocation/', views.getRedundantLocation, name='api-getRedundantLocation'),
    path('getAllRedundant/', views.getAllRedundant, name='api-getAllRedundant'),
    path('addRedundantForLocation/', views.addRedundantForLocation, name='api-addRedundantForLocation'),
    path('editRedundantForLocation/', views.editRedundantForLocation, name='api-editRedundantForLocation'),
    path('deleteRedundantForLocation/', views.deleteRedundantForLocation, name='api-deleteRedundantForLocation'),
    path('addPlace/', views.addPlace, name='api-addPlace'),
    path('getCityList/', views.getCityList, name='api-getCityList'),
    path('getBigCityList/', views.getBigCityList, name='api-getBigCityList'),
    path('getCityPartList/', views.getCityPartList, name='api-getCityPartList'),
    path('getBigVillageList/', views.getBigVillageList, name='api-getBigVillageList'),
    path('getVillageList/', views.getVillageList, name='api-getVillageList'),
    path('deletePlace/', views.deletePlace, name='api-deletePlace'),
    path('editPlace/', views.editPlace, name='api-editPlace'),
    path('getInfoPlace/', views.getInfoPlace, name='api-getInfoPlace'),

    path('getPropertyListByFilter/', views.getPropertyListByFilter, name='api-getPropertyListByFilter'),
    path('getInfoPropertyBToPlace/', views.getInfoPropertyBToPlace, name='api-getInfoPropertyBToPlace'),
    path('deletePropertyBelongToPlace/', views.deletePropertyBelongToPlace, name='api-deletePropertyBelongToPlace'),
    path('getPropertyNameList/', views.getPropertyNameList, name='api-getPropertyNameList'),
    path('getAllSubPropertyNameList/', views.getAllSubPropertyNameList, name='api-getAllSubPropertyNameList'),
    path('getSubPropertyNameList/', views.getSubPropertyNameList, name='api-getSubPropertyNameList'),
    path('addPropertyToPlace/', views.addPropertyToPlace, name='api-addPropertyToPlace'),
    path('editPropertyToPlace/', views.editPropertyToPlace, name='api-editPropertyToPlace'),
    path('addSubProperty/', views.addSubProperty, name='api-addSubProperty'),
    path('editSubProperty/', views.editSubProperty, name='api-editSubProperty'),
    path('deleteSubProperty/', views.deleteSubProperty, name='api-deleteSubProperty'),

    path('getProperList/', views.getProperList, name='api-getProperList'),
    path('getPeopleBelongToPlaceList/', views.getPeopleBelongToPlaceList, name='api-getPeopleBelongToPlaceList'),
    path('getInfoPeopleBelongToPlace/', views.getInfoPeopleBelongToPlace, name='api-getInfoPeopleBelongToPlace'),
    path('addPeopleBelongToPlace/', views.addPeopleBelongToPlace, name='api-addPeopleBelongToPlace'),
    path('editPeopleBelongToPlace/', views.editPeopleBelongToPlace, name='api-editPeopleBelongToPlace'),
    path('deletePeopleBelongToPlace/', views.deletePeopleBelongToPlace, name='api-deletePeopleBelongToPlace'),

    path('getAnswerPropertyBToPlaceList/', views.getAnswerPropertyBToPlaceList,
         name='api-getAnswerPropertyBToPlaceList'),
    path('addAnswerToProperty/', views.addAnswerToProperty, name='api-addAnswerToProperty'),
    path('editAnswerProperty/', views.editAnswerProperty, name='api-editAnswerProperty'),
    path('deleteAnswerProperty/', views.deleteAnswerProperty, name='api-deleteAnswerProperty'),


    path('getFullInfoPropertyBToPlace/', views.getFullInfoPropertyBToPlace, name='api-getFullInfoPropertyBToPlace'),


    path('getUrlExportPropertyToExcel/', views.getUrlExportPropertyToExcel, name='api-getUrlExportPropertyToExcel'),

    path('getAllOrganization/', views.getAllOrganization, name='api-getAllOrganization'),
    path('getSolutionToProperty/', views.getSolutionToProperty, name='api-getSolutionToProperty'),
    path('addSolutionToProperty/', views.addSolutionToProperty, name='api-addSolutionToProperty'),
    path('editSolutionToProperty/', views.editSolutionToProperty, name='api-editSolutionToProperty'),
    path('deleteSolutionToProperty/', views.deleteSolutionToProperty, name='api-deleteSolutionToProperty'),


    path('getAccessListManager/', views.getAccessListManager, name='api-getAccessListManager'),
]

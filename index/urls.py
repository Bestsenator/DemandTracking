from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-index'),
    path('exportPropertyToExcel/<int:code>/', views.exportPropertyToExcel, name='index-exportPropertyToExcel'),
]

from django.shortcuts import render
import pandas as pd
from index.serializers import *
from django.http import HttpResponse

# Create your views here.


def index(request):
    pass


def exportPropertyToExcel(request, code):
    exportListInfo = ExportPropertyList.objects.filter(Code=code).first()
    if exportListInfo:
        listCode = eval(exportListInfo.List)
        propertyInfo = PropertyBelongPlace.objects.filter(Code__in=listCode)
        if propertyInfo:
            propertyInfoSer = PropertyBelongPlaceExcelSer(propertyInfo, many=True).data
            df = pd.DataFrame(propertyInfoSer)
            df.columns = ['کد', 'ویژگی', 'زیرویژگی', 'مکان', 'عنوان', 'توضیحات', 'زمان ثبت']
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="{}.xlsx"'.format(code)
            response['x-ms-excel-direction'] = 'rtl'
            # ذخیره DataFrame در فایل اکسل
            df.to_excel(response, index=False)
            return response
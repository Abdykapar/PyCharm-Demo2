from django.shortcuts import render
from django.http import HttpResponse
import xlrd
from xlrd.sheet import ctype_text
from .models import Bolumder, Lkp_God


def index(request):
    a = Bolumder.objects.get(id=2)
    # file_location = "/media/abdykapar/46E6D1D4E6D1C479/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    return HttpResponse(a.NameKir)


def BolumderAdd():
    # file_location = "/media/abdykapar/46E6D1D4E6D1C479/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/Bolumder.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    inserBolumder(sheet)


def show_column_names(xl_sheet):
    a = []
    row = xl_sheet.row(0)  # 1st row
    print(60*'-' + 'n(Column #) value [type]n' + 60*'-')
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        a.append(' '+cell_obj.value)

        print('(%s) %s [%s]' % (idx, cell_obj.value, cell_type_str, ))

    return a


def inserBolumder(val):
    b = []
    for a in range(1,val.nrows):
        row = val.row(a)
        Bolum = Bolumder(NameOtd=row[1].value, NameTur=row[2].value, NameKir=row[2].value)
        Bolum.save()


def LkpGod(request):
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/Lkp_God.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)


def insertLkpGod(val):
    b = []
    for a in range(1, val.nrows):
        row = val.row(a)
        lkp = Lkp_God(God=row[1].value)
        Bolum.save()
from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
import xlrd
from xlrd.sheet import ctype_text
from .models import Bolumder, Lkp_God, LkpOblast, LkpRayon, MyTable, RayonExp, Pol


def index(request):
    a = Bolumder.objects.get(id=2)
    # file_location = "/media/abdykapar/46E6D1D4E6D1C479/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    return HttpResponse(a.NameKir)


def BolumderAdd(request):
    # file_location = "/media/abdykapar/46E6D1D4E6D1C479/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/Bolumder14.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    bolum = Bolumder.objects.all()
    print bolum.count()
    for i in range(1,bolum.count()+1):
        row = sheet.row(i)
        print row[4].value
        # bolum.filter(id=i).update(Kod=row[4].value)
    # inserBolumder(sheet)
    return HttpResponse('Ok')


def show_column_names(xl_sheet):
    a = []
    row = xl_sheet.row(0)  # 1st row
    print(60 * '-' + 'n(Column #) value [type]n' + 60 * '-')
    for idx, cell_obj in enumerate(row):
        cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
        a.append(' ' + cell_obj.value)

        print('(%s) %s [%s]' % (idx, cell_obj.value, cell_type_str,))

    return a


def inserBolumder(val):
    b = []
    for a in range(1, val.nrows):
        row = val.row(a)
        Bolum = Bolumder(NameOtd=row[1].value, NameTur=row[2].value, NameKir=row[3].value)
        Bolum.save()


def LkpGod(request):
    a = []
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/Lkp_God.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    # insertLkpGod(sheet)
    print (a)
    return HttpResponse(a)


def insertLkpGod(val):
    b = []
    for a in range(1, val.nrows):
        row = val.row(a)
        lkp = Lkp_God(God=row[1].value)
        lkp.save()


def lkpOblast(request):
    b = []
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/LkpOblast14.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    for a in range(1, sheet.nrows):
        row = sheet.row(a)
        # Obl = LkpOblast(NameOblast=row[1].value)
        # Obl.save()

    return HttpResponse(b)


def lkpRayon(request):
    b = []
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/LkpRayon14.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    for a in range(1, sheet.nrows):
        row = sheet.row(a)
        rayon = LkpRayon(Rayon=row[2].value, KodOblast_id=row[1].value)
        rayon.save()

    return HttpResponse(b)


def pol(request):
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/Lkp_Jinisi_3.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    for a in range(1, sheet.nrows):
        row = sheet.row(a)
        print row[1].value
        polEx = Pol(
            PolK=row[1].value, PolR=row[2].value, PolT=row[3].value
        )
        polEx.save()

    return HttpResponse('Ok')


def editTable1(request):
    for i in range(1,6367):
        MyTable.objects.filter(id=5819+i).update(God_Created=2011)
    return HttpResponse('Ok')


def table1(request):
    b = []

    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/2014.xlsx"
    # file_location = "/media/abdykapar/46E6D1D4E6D1C479/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    num2 = int(sheet.row(2)[14].value)
    print(num2)
    print(sheet.row(1)[21].value)
    for i in range(1, sheet.nrows):
        row = sheet.row(i)
        for a , x in enumerate(row):
            if x.value == '':
                x.value = 1

        print row[24].value
        if row[13].value == '':
            row[13].value = 1
        lkO = LkpOblast.objects.get(pk=row[13].value)
        if row[14].value == '':
            row[14].value = 1
        lkR = LkpRayon.objects.get(pk=row[14].value)
        if row[16].value == '':
            row[16].value = 1
        homeO = LkpOblast.objects.get(pk=row[16].value)
        if row[17].value == '':
            row[17].value = 1
        homeR = LkpRayon.objects.get(pk=int(row[17].value))
        if row[21].value == '':
            row[21].value = 1
        god = Lkp_God.objects.get(pk=row[21].value)
        if row[61].value == '':
            row[61].value = 1
        tercih = Bolumder.objects.get(pk=row[61].value)
        if row[59].value == '':
            row[59].value = 1
        otd = Bolumder.objects.get(pk=row[59].value)
        table1 = MyTable(
            Sifra = row[1].value, NameN=row[2].value, Surname=row[3].value, Lastname=row[4].value, Pol=row[7].value, Dr=row[8].value, Nas=row[11].value,
            Sh=row[12].value, Adress_Sh_Oblast=lkO, Adress_Sh_Rayon=lkR, Adress_Sh_Selo=row[15].value,
            Adress_Home_Oblast=homeO, Adress_Home_Rayon=homeR, Adress_Home_Selo=row[18].value, Adress_Home_Ulisa=row[19].value,
            Telefon=row[20].value, God=god,
            t1=row[23].value, t2=row[24].value, t3=row[25].value, t4=row[26].value, t5=row[27].value, PolePrav=row[31].value, PoleNeprav=row[32].value,
            PoleProbel=row[33].value, SozD=row[34].value, SozY=row[35].value, SozB=row[36].value, SayD=row[37].value, SayY=row[38].value,
            SayB=row[39].value, DilD=row[40].value, DilY=row[41].value, DilB=row[42].value, NetSay=row[43].value, NetSoz=row[44].value,
            NetDil=row[45].value, SrSay=row[46].value, SrSoz=row[47].value, SrDil=row[48].value, SSay=row[49].value, SSoz=row[50].value,
            SDil=row[51].value, StdSay=row[52].value, StdSoz=row[53].value, StdDil=row[54].value, EA=row[55].value, SonSoz=row[56].value,
            SonSay=row[57].value, SonDil=row[58].value, Otdelenie=otd, NomTerciha=tercih, God_Created=2014)
        table1.save()

    return HttpResponse('Ok')


def ExpRayon(request):
    # file_location = "/media/abdykapar/46E6D1D4E6D1C479/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        row = sheet.row(i)
        exp1 = LkpRayon.objects.get(pk=1)
        exp = RayonExp(
            Name='My name', ExpName=exp1
        )
        exp.save()
    return HttpResponse('Ok')

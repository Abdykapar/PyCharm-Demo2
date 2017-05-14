from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal
import xlrd
from xlrd.sheet import ctype_text
from .models import iv, Bolumder, last, Lkp_God, LkpOblast, LkpRayon, MyTable, RayonExp, Pol, averageBol


def index(request):
    # file_location = "/media/abdykapar/46E6D1D4E6D1C479/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    return render(request, 'app/index.html')


def averageOfBolumOrun(bolumder):
    sum = 0
    count  = bolumder.count() - 1
    for bolum in bolumder:
        sum = sum + bolum.Orun
    return sum/count


def percentStd(average_bolumder, std):
    all_std = MyTable.objects.all().count()
    jalpi_nom_std = all_std - std.id
    bolumder = Bolumder.objects.all()
    std_num = MyTable.objects.filter(God_Created=2014).count()
    std_percent_total = std_num / average_bolumder
    nom_std = std_num - jalpi_nom_std
    std_percent_single = nom_std / average_bolumder * 100 / std_percent_total
    return 100 - std_percent_single


def findAve(std):
    ordu = 0
    ave = averageBol.objects.all().order_by('-average')
    for a in ave:
        if a.averageBolId.Type == 'EA':
            if std.EA >= a.average:
                ordu = a.id

    return ordu

def bolumPercentChance(std):
    percentage = 0
    ave = averageBol.objects.all().order_by('-average')
    count = ave.count()
    stdAveOrdu = findAve(std)

    for a in ave:
        if a.averageBolId.Type == "EA":
            if std.EA >= a.average:
                percentage = 100
            else :
                percentage = 100 * stdAveOrdu

def get_id(request):
    s = Decimal
    std = MyTable.objects.get(Sifra=request.GET['id'])
    items = MyTable.objects.filter(God_Created=2014)
    bolumder = Bolumder.objects.all()
    s = averageOfBolumOrun(bolumder)
    pStd = percentStd(s, std)
    pBol = bolumPercentChance(std)

    return render(request, 'app/show.html')


def bolumMinMax(request):
    bolumder = Bolumder.objects.filter()


def popular(request):
    checked = []
    bolumder = Bolumder.objects.all().order_by('-NumTandoo')
    items = MyTable.objects.filter(God_Created=2014)
    # for bolum in bolumder:
    #     i = 0
    #     if bolum.Type == 'EA':
    #         print bolum.NameOtd
    #         items = MyTable.objects.filter(God_Created=2014).order_by('-EA')
    #         for item in items:
    #             if item.Sifra not in checked:
    #                 lst = last(student=item, bolum=bolum, mesto=i+1, ball=item.EA)
    #                 lst.save()
    #                 print item.NameN
    #                 checked.append(item.Sifra)
    #                 i += 1
    #             if bolum.Orun == i:
    #                 break
    #     elif bolum.Type == 'SonSay':
    #         print bolum.NameOtd
    #         items = MyTable.objects.filter(God_Created=2014).order_by('-SonSay')
    #         for item in items:
    #             if item.Sifra not in checked:
    #                 print item.NameN
    #                 lst = last(student=item, bolum=bolum, mesto=i+1, ball=item.SonSay)
    #                 lst.save()
    #                 i += 1
    #                 checked.append(item.Sifra)
    #             if bolum.Orun == i:
    #                 break
    #     elif bolum.Type == 'SonSoz':
    #         print bolum.NameOtd
    #         items = MyTable.objects.filter(God_Created=2014).order_by('-SonSoz')
    #         for item in items:
    #             if item.Sifra not in checked:
    #                 print item.NameN
    #                 lst = last(student=item, bolum=bolum, mesto=i+1, ball=item.SonSoz)
    #                 lst.save()
    #                 i += 1
    #                 checked.append(item.Sifra)
    #             if bolum.Orun == i:
    #                 break
    data = last.objects.all()
    ave = averageBol.objects.all()
    return render(request, 'app/statisticsView.html', {'data': data, 'average': ave})


def test(request):
    sum = 0
    items = MyTable.objects.filter(God_Created=2014)
    all_std = MyTable.objects.all().count()
    std = MyTable.objects.get(Sifra=14210874)
    jalpi_nom_std = all_std-std.id
    bolumder = Bolumder.objects.all()
    for bolum in bolumder:
        sum += bolum.Orun
    average_bolumder = sum/(bolumder.count()-1)
    print all_std
    print sum
    print average_bolumder
    std_num = MyTable.objects.filter(God_Created=2014).count()
    std_percent_total = std_num/average_bolumder
    print std_num
    nom_std = std_num - jalpi_nom_std
    print nom_std
    print nom_std/average_bolumder
    std_percent_single = nom_std/average_bolumder * 100 / std_percent_total
    print 100 - std_percent_single
    return render(request, 'app/test.html', {'items': items})


def average(request):
    l = []
    minElement = Decimal
    maxElement = Decimal
    ortolama = Decimal
    bolumder = Bolumder.objects.all()
    items = MyTable.objects.all()
    for bolum in bolumder:
        a = MyTable.objects.filter(Otdelenie_id=bolum, God_Created__gte=2012)
        print bolum
        for c in a:
            if bolum.Type == 'EA':
                l.append(c.EA)
            elif bolum.Type == 'SonSay':
                l.append(c.SonSay)
            elif bolum.Type == 'SonSoz':
                l.append(c.SonSoz)
        if len(l) > 0:
            minElement = min(l)
            maxElement = max(l)
        else:
            maxElement = 0
            minElement = 0
        l = []
        ave = averageBol.objects.get(averageBolId=bolum)
        ave.maxElement = maxElement
        ave.minElement = minElement
        ave.save()
    # for bolum in bolumder:
    #     print "Bolum: " + bolum.NameOtd
    #     items = MyTable.objects.filter(Otdelenie_id=bolum)
    #     for item in items:
    #         if item.God_Created >= 2012:
    #             if bolum.Type == "SonSay":
    #                 l.append(item.SonSay)
    #             elif bolum.Type == "SonSoz":
    #                 l.append(item.SonSoz)
    #             elif bolum.Type == "EA":
    #                 l.append(item.EA)
    #     if len(l) > 0:
    #         ortolama = sum(l)/len(l)
    #     else:
    #         ortolama = 0
    #     print "Average: " + unicode(ortolama)
    #     aBol = averageBol.objects.get(averageBolId=bolum)
    #     aBol.average = ortolama
    #     aBol.save()
    #     l = []
    ab = averageBol.objects.all().order_by('-average')
    return render(request, 'app/average.html', {'ab': ab})


def takeBall(item, type):
    l = Decimal
    print type
    if type == "SonSay":
        l = item.SonSay
    elif type == "SonSoz":
        l = item.SonSoz
    elif type == "EA":
        l = item.EA
    return l


def TandooSort():
    items = MyTable.objects.order_by()
    bolum = Bolumder.objects.order_by('-NumTandoo')
    # for bol in bolum:
    #     bol.NumTandoo = 0
    #     bol.save()
    # for bol in bolum:
    #     print bol.id
    #     for item in items:
    #         if item.t1 == bol.Kod:
    #             bol.NumTandoo += 1
    #             bol.save()
    #         if item.t2 == bol.Kod:
    #             bol.NumTandoo += 1
    #             bol.save()
    #         if item.t3 == bol.Kod:
    #             bol.NumTandoo += 1
    #             bol.save()
    #         if item.t4 == bol.Kod:
    #             bol.NumTandoo += 1
    #             bol.save()
    #         if item.t5 == bol.Kod:
    #             bol.NumTandoo += 1
    #             bol.save()
    return bolum


def BolumderAdd(request):
    # file_location = "/media/abdykapar/46E6D1D4E6D1C479/FUTURE/lESSON/DIPLOM/sinav/table1.xlsx"
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/Bolumder14.xlsx"
    book = xlrd.open_workbook(file_location)
    sheet = book.sheet_by_index(0)
    bolum = Bolumder.objects.all()
    print bolum.count()
    for i in range(1, bolum.count() + 1):
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
    for i in range(1, 6367):
        MyTable.objects.filter(id=5819 + i).update(God_Created=2011)
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
    # for i in range(1, sheet.nrows):
    #     row = sheet.row(i)
    #     for a, x in enumerate(row):
    #         if x.value == '':
    #             x.value = 1
    #
    #     print row[24].value
    #     if row[13].value == '':
    #         row[13].value = 1
    #     lkO = LkpOblast.objects.get(pk=row[13].value)
    #     if row[14].value == '':
    #         row[14].value = 1
    #     lkR = LkpRayon.objects.get(pk=row[14].value)
    #     if row[16].value == '':
    #         row[16].value = 1
    #     homeO = LkpOblast.objects.get(pk=row[16].value)
    #     if row[17].value == '':
    #         row[17].value = 1
    #     homeR = LkpRayon.objects.get(pk=int(row[17].value))
    #     if row[21].value == '':
    #         row[21].value = 1
    #     god = Lkp_God.objects.get(pk=row[21].value)
    #     if row[61].value == '':
    #         row[61].value = 1
    #     tercih = Bolumder.objects.get(pk=row[61].value)
    #     if row[59].value == '':
    #         row[59].value = 1
    #     otd = Bolumder.objects.get(pk=row[59].value)
    #     table1 = MyTable(
    #         Sifra=row[1].value,
    #         NameN=row[2].value,
    #         Surname=row[3].value,
    #         Lastname=row[4].value,
    #         Pol=row[7].value,
    #         Dr=row[8].value,
    #         Nas=row[11].value,
    #         Sh=row[12].value,
    #         Adress_Sh_Oblast=lkO,
    #         Adress_Sh_Rayon=lkR,
    #         Adress_Sh_Selo=row[15].value,
    #         Adress_Home_Oblast=homeO,
    #         Adress_Home_Rayon=homeR,
    #         Adress_Home_Selo=row[18].value,
    #         Adress_Home_Ulisa=row[19].value,
    #         Telefon=row[20].value,
    #         God=god,
    #         t1=row[23].value,
    #         t2=row[24].value,
    #         t3=row[25].value,
    #         t4=row[26].value,
    #         t5=row[27].value,
    #         PolePrav=row[31].value,
    #         PoleNeprav=row[32].value,
    #         PoleProbel=row[33].value, SozD=row[34].value, SozY=row[35].value, SozB=row[36].value, SayD=row[37].value,
    #         SayY=row[38].value,
    #         SayB=row[39].value, DilD=row[40].value, DilY=row[41].value, DilB=row[42].value, NetSay=row[43].value,
    #         NetSoz=row[44].value,
    #         NetDil=row[45].value, SrSay=row[46].value, SrSoz=row[47].value, SrDil=row[48].value, SSay=row[49].value,
    #         SSoz=row[50].value,
    #         SDil=row[51].value, StdSay=row[52].value, StdSoz=row[53].value, StdDil=row[54].value, EA=row[55].value,
    #         SonSoz=row[56].value,
    #         SonSay=row[57].value, SonDil=row[58].value, Otdelenie=otd, NomTerciha=tercih, God_Created=2014)
    #     table1.save()

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

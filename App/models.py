from __future__ import unicode_literals

from django.db import models


class Bolumder(models.Model):
    NameOtd = models.CharField(max_length=200)
    NameTur = models.CharField(max_length=200)
    NameKir = models.CharField(max_length=200)


class Lkp_God(models.Model):
    God = models.IntegerField()


class LkpOblast(models.Model):
    NameOblast = models.CharField(max_length=200)


class LkpRayon(models.Model):
    KodOblast = models.ForeignKey(LkpOblast, on_delete=models.CASCADE)
    Rayon = models.CharField(max_length=200)



class MyTable(models.Model):
    Sifra = models.IntegerField(default=0)
    NameN = models.CharField(max_length=200, default='')
    Surname = models.CharField(max_length=200, default='')
    Lastname = models.CharField(max_length=200, default='')
    Korpus = models.CharField(max_length=200, default='')
    Pol = models.CharField(max_length=200, default='')
    Dr = models.DateTimeField('data rojdeniya', blank=True, null=True)
    Nas = models.CharField(max_length=200, default='')
    Sh = models.CharField(max_length=200, default='')
    Adress_Sh_Oblast = models.CharField(max_length=200, default='')
    Adress_Sh_Rayon = models.CharField(max_length=200, default='')
    Adress_Sh_Selo = models.CharField(max_length=200, default='')
    Adress_Home_Oblast = models.CharField(max_length=200, default='')
    Adress_Home_Rayon = models.CharField(max_length=200, default='')
    Adress_Home_Selo = models.CharField(max_length=200, default='')
    Adress_Home_Ulisa = models.CharField(max_length=200, default='')
    Telefon = models.CharField(max_length=200, default='')
    God = models.CharField(max_length=200, default='')
    t1 = models.CharField(max_length=200, default='')
    t2 = models.CharField(max_length=200, default='')
    t3 = models.CharField(max_length=200, default='')
    t4 = models.CharField(max_length=200, default='')
    t5 = models.CharField(max_length=200, default='')
    PolePrav = models.IntegerField(default=0)
    PoleNeprav = models.IntegerField(default=0)
    PoleProbel = models.IntegerField(default=0)
    SozD = models.IntegerField(default=0)
    SozY = models.IntegerField(default=0)
    SozB = models.IntegerField(default=0)
    SayD = models.IntegerField(default=0)
    SayY = models.IntegerField(default=0)
    SayB = models.IntegerField(default=0)
    DilD = models.IntegerField(default=0)
    DilY = models.IntegerField(default=0)
    DilB = models.IntegerField(default=0)
    NetSay = models.IntegerField(default=0)
    NetSoz = models.IntegerField(default=0)
    NetDil = models.IntegerField(default=0)
    SrSay = models.IntegerField(default=0)
    SrSoz = models.IntegerField(default=0)
    SrDil = models.IntegerField(default=0)
    SSay = models.IntegerField(default=0)
    SSoz = models.IntegerField(default=0)
    SDil = models.IntegerField(default=0)
    StdSay = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    StdSoz = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    StdDil = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    EA = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    SonSoz = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    SonSay = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    Son = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    SonDil = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    Otdelenie = models.CharField(max_length=200, default='')
    NomTerciha = models.IntegerField(default=0)
    DilSinav = models.IntegerField(default=0)






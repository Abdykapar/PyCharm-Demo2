from __future__ import unicode_literals

from django.db import models


class Bolumder(models.Model):
    NameOtd = models.CharField(max_length=100)
    NameTur = models.CharField(max_length=200)
    NameKir = models.CharField(max_length=200)
    Kod = models.IntegerField(default=0, unique=True)
    NumTandoo = models.IntegerField(default=0)
    Type = models.CharField(max_length=100, default='')
    Orun = models.IntegerField(default=0)

    def __unicode__(self):
        return self.NameOtd


class Lkp_God(models.Model):
    God = models.IntegerField()

    def __unicode__(self):
        return self.God


class LkpOblast(models.Model):
    NameOblast = models.CharField(max_length=200)

    def __unicode__(self):
        return self.NameOblast


class LkpRayon(models.Model):
    KodOblast = models.ForeignKey(LkpOblast, on_delete=models.CASCADE)
    Rayon = models.CharField(max_length=200)

    def __unicode__(self):
        return self.KodOblast


class Pol(models.Model):
    PolK = models.CharField(max_length=200)
    PolR = models.CharField(max_length=200)
    PolT = models.CharField(max_length=200)

    def __unicode__(self):
        return self.PolR


class MyTable(models.Model):
    Sifra = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    NameN = models.CharField(max_length=200)
    Surname = models.CharField(max_length=200)
    Lastname = models.CharField(max_length=200)
    Korpus = models.CharField(max_length=200)
    Pol = models.CharField(max_length=200)
    Dr = models.CharField(max_length=200, blank=True, null=True)
    Nas = models.CharField(max_length=200, blank=True, null=True)
    Sh = models.CharField(max_length=200, blank=True, null=True)
    Adress_Sh_Oblast = models.ForeignKey(LkpOblast, on_delete=models.CASCADE, related_name='address_sh_oblast')
    Adress_Sh_Rayon = models.ForeignKey(LkpRayon, on_delete=models.CASCADE, related_name='address_sh_rayon')
    Adress_Sh_Selo = models.CharField(max_length=200, blank=True, null=True)
    Adress_Home_Oblast = models.ForeignKey(LkpOblast, on_delete=models.CASCADE, related_name='address_home_oblast')
    Adress_Home_Rayon = models.ForeignKey(LkpRayon, on_delete=models.CASCADE, related_name='address_home_rayon')
    Adress_Home_Selo = models.CharField(max_length=200, blank=True, null=True)
    Adress_Home_Ulisa = models.CharField(max_length=200, blank=True, null=True)
    Telefon = models.CharField(max_length=200, blank=True, null=True)
    God = models.ForeignKey(Lkp_God, on_delete=models.CASCADE)
    t1 = models.IntegerField(null=True, blank=True)
    t2 = models.IntegerField(null=True, blank=True)
    t3 = models.IntegerField(null=True, blank=True)
    t4 = models.IntegerField(null=True, blank=True)
    t5 = models.IntegerField(null=True, blank=True)
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
    StdSay = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    StdSoz = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    StdDil = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    EA = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    SonSoz = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    SonSay = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    Son = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    SonDil = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    Otdelenie = models.ForeignKey(Bolumder, null=True, related_name='otdelenie')
    NomTerciha = models.ForeignKey(Bolumder, null=True, related_name='nomTerciha')
    DilSinav = models.IntegerField(default=0)
    God_Created = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.NameN


class RayonExp(models.Model):
    Name = models.CharField(max_length=200)
    ExpName = models.ForeignKey(LkpRayon)

    def __unicode__(self):
        return self.Name


class iv(models.Model):
    name = models.ForeignKey(Bolumder)
    bolum_pop = models.IntegerField(default=0)
    bolum_average = models.DecimalField(max_digits=12, decimal_places=6, blank=True)
    jer_id = models.ForeignKey(LkpOblast)

    def __unicode__(self):
        return self.name


class averageBol(models.Model):
    averageBolId = models.ForeignKey(Bolumder)
    average = models.DecimalField(max_digits=8, decimal_places=4, blank=True)
    maxElement = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    minElement = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    chanse = models.DecimalField(max_digits=8, decimal_places=4, default=0)

    def __unicode__(self):
        return self.average


class last(models.Model):
    student = models.ForeignKey(MyTable)
    bolum = models.ForeignKey(Bolumder)
    mesto = models.IntegerField(default=0)
    ball = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    average = models.ForeignKey(averageBol,default=1)

    def __unicode__(self):
        return self.student.NameN


class Detail(models.Model):
    student = models.ForeignKey(MyTable)
    bolum = models.ForeignKey(Bolumder)
    chance = models.DecimalField(max_digits=8, decimal_places=4, default=0)

    def __unicode__(self):
        return self.chance
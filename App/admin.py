from django.contrib import admin
from .models import Bolumder, MyTable, LkpOblast, LkpRayon, Lkp_God, RayonExp


class BolumderAdmin(admin.ModelAdmin):
    fields = ['NameOtd', 'NameKir']
    list_display = ('NameOtd', 'NameKir')


admin.site.register(Bolumder)
admin.site.register(MyTable)
admin.site.register(Lkp_God)
admin.site.register(LkpOblast)
admin.site.register(LkpRayon)
admin.site.register(RayonExp)
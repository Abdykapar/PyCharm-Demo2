from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^bolum$', views.BolumderAdd , name='Bolum'),
    url(r'^lkpGod$', views.LkpGod, name='lkpGod'),
    url(r'^lkpOblast$', views.lkpOblast, name='lkpOblast'),
    url(r'^lkpRayon$', views.lkpRayon, name='lkpRayon'),
    url(r'^table1', views.table1, name='table1'),
    url(r'^Edittable1', views.editTable1, name='edittable1'),
    url(r'^exp1', views.ExpRayon, name='exp1'),
    url(r'^pol$', views.pol, name='pol'),
]
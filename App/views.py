from django.shortcuts import render
from django.http import HttpResponse
import xlrd


def index(request):
    file_location = "D:/FUTURE/lESSON/DIPLOM/sinav/2010.xlsx"
    workbook = xlrd.open_workbook(file_location)
    return HttpResponse('Hello world')

from django.shortcuts import render
from django.http import HttpResponse
from .models import LoaiSanPham
# Create your views here.

def home_view(request,*args,**kwags):
    return render(request,"index.html",{})


def LoaiSanPham_Menu(request,*args,**kwags):
    pass
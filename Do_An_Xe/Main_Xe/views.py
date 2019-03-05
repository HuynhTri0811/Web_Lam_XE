from django.shortcuts import render
from django.http import HttpResponse
from .models import LoaiSanPham
# Create your views here.
List_Menu_SanPham = LoaiSanPham.objects.filter(BiXoa=0)
my_context = {
    'List_Menu_SanPham' : List_Menu_SanPham,
    'content' : 'abc' 
}
def home_view(request,*args,**kwags):
    
    return render(request,"index.html",my_context)


def LoaiSanPham_Menu(request,MaLoaiSanPham):
    if MaLoaiSanPham == 1:
        return render(request,"loaiSanPhamDienThoai.html",my_context)
    else :
        return render(request,"erorr.html")
    
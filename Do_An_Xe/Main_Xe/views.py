from django.shortcuts import render
from django.http import HttpResponse
from .models import LoaiSanPham,HangSanXuat
# Create your views here.
List_Menu_LoaiSanPham = LoaiSanPham.objects.filter(BiXoa=0)
List_Menu_HangSanXuat = HangSanXuat.objects.filter(BiXoa=0)

my_context = {
    'List_Menu_LoaiSanPham' : List_Menu_LoaiSanPham,
    'List_Menu_HangSanXuat' : List_Menu_HangSanXuat,
}
def home_view(request,*args,**kwags):
    return render(request,"index.html",my_context)


def LoaiSanPham_Menu(request,MaLoaiSanPham):
    if MaLoaiSanPham == 1:
        return render(request,"Menu_LoaiSanPham/loaiSanPhamDienThoai.html",my_context)
    elif MaLoaiSanPham == 2:
        return render(request,"Menu_LoaiSanPham/loaiSanPhamMayTinhBang.html",my_context)
    elif MaLoaiSanPham == 3:
        return render(request,"Menu_LoaiSanPham/loaiSanPhamTayNghe.html",my_context)
    elif MaLoaiSanPham == 4:
        return render(request,"Menu_LoaiSanPham/loaiSanPhamDoSac.html",my_context)
    else :
        return render(request,"erorr.html")

def HangSanXuat_Menu(request,MaHangSanXuat):
    if MaHangSanXuat == 1:
        return render(request,"Menu_HangSanXuat/HangSanXuatSamSung.html",my_context)
    elif MaHangSanXuat == 2:
        return render(request,"Menu_HangSanXuat/HangSanXuatOPPO.html",my_context)
    elif MaHangSanXuat == 3:
        return render(request,"Menu_HangSanXuat/HangSanXuatXiaomi.html",my_context)
    elif MaHangSanXuat == 4:
        return render(request,"Menu_HangSanXuat/HangSanXuatIphone.html",my_context)
    elif MaHangSanXuat == 5:
        return render(request,"Menu_HangSanXuat/HangSanXuatNokia.html",my_context)
    else :
        return render(request,"erorr.html")
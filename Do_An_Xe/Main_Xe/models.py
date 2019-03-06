from django.db import models

# Create your models here.
class LoaiSanPham(models.Model):
    MaLoaiSanPham   = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID_Hang')
    TenLoaiSanPham  = models.CharField(max_length=100)
    BiXoa           = models.IntegerField(default=0)

    def __str__(self):
        return  str(self.MaLoaiSanPham)+ " - " + self.TenLoaiSanPham

class HangSanXuat(models.Model):
    MaHangSanXuat   = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID_HangSanXuat")
    TenHangSanXuat  = models.CharField(max_length=100)
    HinhURL_HSX     = models.ImageField(upload_to='Node',blank=True)
    BiXoa           = models.IntegerField(default=0) 

    def __str__(self):
        return str(self.MaHangSanXuat)+ " - " + self.TenHangSanXuat


class SanPham(models.Model):
    MaSanPham       = models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID_Xe')
    TenSanPham      = models.CharField(max_length=100)
    HinhURL         = models.CharField(max_length=100,null=True)
    GiaSanPham      = models.IntegerField(default=0)
    SoLuongTon      = models.IntegerField(default=0)
    SoLuongBan      = models.IntegerField(default=0)
    SoLuotXem       = models.IntegerField(default=0)
    MoTa            = models.TextField()
    BiXoa           = models.IntegerField(default=0)
    MaLoaiSanPham   = models.ForeignKey(LoaiSanPham,on_delete=models.CASCADE,related_name='ID_LoaiSanPham')
    MaHangSanXuat   = models.ForeignKey(HangSanXuat,on_delete=models.CASCADE,related_name='ID_HangSanXuat')
from sinhvien import SinhVien
n=input("Nhap so sinh vien: ")
sv = []
for i in range(0,n):
	Ten=input("nhap ten: ")
	NamSinh=input("nhap nam sinh: ")
	Khoa=input("nhap khoa: ")
	ds=SinhVien(Ten,NamSinh,Khoa)
	sv.append(ds)

for i in sv:
	#print 'Thong tin sv thu ',i
	print(i.toString())


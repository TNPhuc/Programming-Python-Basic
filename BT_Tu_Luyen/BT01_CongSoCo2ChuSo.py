"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Viết chương trình cộng các số của số có 2 chữ số. Ví dụ: nếu đầu vào là 35, thì đầu ra phải là 3 + 5 = 8
"""

# Đầu vào: Nhập vào số N có 2 chữ số
N = int(input("Nhap vao so N co 2 chu so: "))
# Tạo điều kiện nhập
if(N<10):
    print("Khong phai so co 2 chu so")
    N = int(input("Nhap lai N: "))
elif(N>99):
    print("Khong phai so co 2 chu so")
    N = int(input("Nhap lai N: "))
# Tạo phép tính
chuc = N // 10
donvi = N % 10
ketqua = chuc + donvi
# Đầu ra
print("Tong cac so co 2 chu so: ", ketqua)

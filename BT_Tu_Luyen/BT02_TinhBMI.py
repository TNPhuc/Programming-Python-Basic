"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Tính chỉ số BMI cơ thể. Công thức: BMI=weight/height^2
"""

# Đầu vào: Khai báo kiểu dữ liệu, nhập vào cân nặng và chiều cao
Weight = float(input("Nhập vào cân nặng của mày đi con hêu: "))
Height = float(input("Nhập cái chiều cao nữa: "))
# Tạo công thức tính chỉ số BMI
BMI = Weight/(Height**2)
# Đầu ra: vừa số thực vừa số nguyên
print("Chỉ số BMI: ", BMI)
print(int(BMI))
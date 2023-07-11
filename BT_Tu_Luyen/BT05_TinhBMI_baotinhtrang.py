"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Tính chỉ số BMI cơ thể. Công thức: BMI=weight/height^2 và báo tình trạng gầy, thừa cân, bình thường
"""

# Đầu vào: Khai báo kiểu dữ liệu, nhập vào cân nặng và chiều cao
Weight = float(input("Nhập cân nặng của mày vào đây đi con điên: "))
Height = float(input("Nhập cả cái chiều cao của mày nữa: "))
# Tạo công thức tính chỉ số BMI
BMI = Weight/(Height**2)
BMI_N = int(BMI)
# Đầu ra: vừa số thực vừa số nguyên
print("BMI của mày tao tính ra được là ", BMI)
#print("Tao làm tròn thành ", BMI_N)
# Thêm điều kiện đầu ra
if(BMI_N < 18.5):
    print(f"Tao làm tròn thành {BMI_N}. Mày ốm nhách dị á!!")
elif(18.5 <= BMI_N < 25):
    print(f"Tao làm tròn thành {BMI_N}. Tỷ lệ cân đối. Good!!")
elif(25 <= BMI_N < 30):
    print(f"Tao làm tròn thành {BMI_N}. Ê ê, Tao thấy mày hơi giống hêu rồi đấy =))")
elif(30 <= BMI_N < 35):
    print(f"Tao làm tròn thành {BMI_N}. Mô phật. Tao thấy mày mập hơn con hêu rồi đấy nhá =)))")
elif(BMI_N >= 35):
    print(f"Tao làm tròn thành {BMI_N}. Trời ơi là trời. Mày còn hơn cái xe lu nữa, Tao thấy mà tao muốn liệt lâm sàn :)")
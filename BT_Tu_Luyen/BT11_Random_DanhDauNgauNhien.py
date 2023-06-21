"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Đánh dấu ngẫu nhiên trên ma trận khi biết cột và hàng
"""

# Khai báo thư viện
import random
# Đầu vào: tạo ma trận
dong1 = ["O","O","O"]
dong2 = ["O","O","O"]
dong3 = ["O","O","O"]
matran = [dong1, dong2, dong3]
# Xuất ra ma trận
print(f"{dong1}\n{dong2}\n{dong3}")
DinhVi = input("Bạn muốn đánh dấu ở vị trí hàng nào cột nào?\n")
# Tách giá trị hàng cột
Hang = int(DinhVi[0])
Cot = int(DinhVi[1])

matran[Hang -1][Cot -1] = "X"
# Đầu ra
print(f"{dong1}\n{dong2}\n{dong3}")
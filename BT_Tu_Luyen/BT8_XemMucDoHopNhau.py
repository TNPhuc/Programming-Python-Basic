"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Xem mức độ hợp nhau dựa vào 2 tên bằng cách đếm số lần chữ cái xuất hiện trong tên trùng với từ TRUE LOVE rồi cộng 2 số lại
"""

print("Chào mừng đến với Thầy Bói Viễn Thông!!")
# Đầu vào: nhập tên 2 người
Female = input("Tên của nhà ngươi là gì?\n")
Male = input("Tên của nữ nhân kia là gì?\n")
# Tạo một biến cộng 2 tên lại để dò số lần xuất hiện các ký tự
Gom = Female + Male
# Đếm số lần xuất hiện các chữ theo TRUE LOVE
T = Gom.count("T")
R = Gom.count("R")
U = Gom.count("U")
E = Gom.count("E")
TRUE = T + R + U + E
L = Gom.count("L")
O = Gom.count("O")
V = Gom.count("V")
E = Gom.count("E")
LOVE = L + O + V + E

TRUE_LOVE = str(TRUE) + str(LOVE)
ScoreLove = int(TRUE_LOVE)
# Điều kiện tính điểm và xuất ra màn hình
if((ScoreLove < 10) or (ScoreLove > 90)):
    print(f"Your score is {ScoreLove}. You go together like coke and mentos.")
elif(40 < ScoreLove < 50):
    print(f"Your score is {ScoreLove}. You are alright together.")
else:
    print(f"Your score is {ScoreLove}.")
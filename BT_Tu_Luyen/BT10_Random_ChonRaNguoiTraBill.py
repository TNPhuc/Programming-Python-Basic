"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Chọn ngẫu nhiên một tên từ danh sách các tên để trả tiền bill
"""

import random
import string
# Đầu vào: nhập tên cách nhau bởi dấu ,
List_name = input("Nhập tên các thành viên. Lưu ý: cách nhau bởi dấu phẩy!\n")
# Các ký tự ngoài dấu ", " sẽ là chuỗi
Name = List_name.split(", ")
# sample () Trả về một mẫu đã cho của một chuỗi
Chon_name = random.sample(Name, 1)
print(f'{Chon_name[0]} is going to buy the meal today!')
"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Xây dựng một chương trình bán hàng tự động, tính tiền hóa đơn dựa trên đơn đặt hàng của khách
        Giá cả như sau:
        Pizza size S: $15; M: $20; L: $25
        Pepperoni for Pizza size S: +$2; for Pizza size M and L: +$3
        Cheese for all size: +$1
"""

# Đầu vào: size Pizza
Size = input("Mày muốn Pizza size mấy theo menu?\n")
# Ban đầu cho tổng bill bằng 0, sau khi chọn các món ta sẽ cộng lên
Bill = 0
# Điều kiện chọn món
if(Size == "S"):
    Total_Bill = Bill + 15
elif(Size == "M"):
    Total_Bill = Bill + 20
elif(Size == "L"):
    Total_Bill = Bill + 25
# Đầu vào: Chọn thêm món
Add_pepperoni = input("Mày có muốn thêm Pepperoni không?\n")
Extra_Cheese = input("Mày có muốn thêm Phô mai không hả?\n")
# Điều kiện cộng thêm bill
if(Add_pepperoni == "Y"):
    if(Size == "S"):
        Total_Bill += 2
    else:
        Total_Bill += 3
elif(Add_pepperoni == "N"):
    Total_Bill += 0

if(Extra_Cheese == "Y"):
    Total_Bill += 1
elif(Extra_Cheese == "N"):
    Total_Bill += 0 

# Đầu ra: hiển thị kết quả Total bill ra màn hình
print(f"Tổng cộng: ${Total_Bill}")

"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Viết chương trình kiểm tra một năm có phải năm nhuận hay không, bằng cách: năm nhuận chia hết cho 4, 100 và 400
"""

# Đầu vào: Nhập vào năm để kiểm tra
Year = int(input("Mày muốn kiểm tra năm nào: "))
# Tạo điều kiện kiểm tra năm có phải năm nhuận hay không
# Đầu ra: trả về kết quả
if((Year % 4 == 0) or (Year % 100 == 0) and (Year % 400 == 0)):
    print("Leap Year (Năm Nhuận nha mạy)")
else:
    print("Not Leap Year (Không phải năm nhuận đâu nha mạy)")
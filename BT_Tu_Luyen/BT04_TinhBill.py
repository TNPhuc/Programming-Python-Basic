"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Tính số tiền phải trả khi bo thêm tiền cho nhân viên
        Ví dụ tiền bill là 150.00$ mà có 5 người, bo có các mức 10%, 12% và 15%
        Tiền bo sẽ tính trên tổng bill
        Tính số tiền mỗi người cần trả, trả về định dạng làm tròn 2 chữ số thập phân
"""

# Khởi tạo đầu vào
print("Chào mừng đến với cách tính tiền Bo của riêng Thầy!")
print("Hãy cho Thầy biết tổng bill của mày bao nhiêu tiền!")
Tien_bill = float(input("$"))
print("Mày muốn Bo cho nhân viên bao nhiêu %: 10%, 12% và 15% ?")
Chiet_khau = int(input())
print("Mày đi bao nhiêu người?")
Nguoi = int(input())
Tong_Chiet_khau = (Chiet_khau / 100) * Tien_bill
Tien_Moi_nguoi = (Tong_Chiet_khau + Tien_bill) / Nguoi
# Làm tròn đến 2 chữ số thập phân tiền cần trả
Tienphaitra = float("{:.2f}".format(Tien_Moi_nguoi))
# Đầu ra
print(f"Mỗi thằng phải trả là ${Tienphaitra}")
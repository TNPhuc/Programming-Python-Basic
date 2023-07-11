"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
-----> Tính Period còn sống sót nếu như sống đến 90 năm cuộc đời
"""

# Đầu vào: Khai báo và nhập dữ liệu
print("Chào mừng mày đã đến vũ trụ của Thầy")
Tuoihientai = int(input("Mày hãy cho Thầy biết mày bao nhiêu tuổi: "))
# Tính số tháng tuần ngày tồn tại trong 90 năm
SoYearTonTaiTrenTheEarth = 90
SoMonthTonTaiTrenTheEarth = SoYearTonTaiTrenTheEarth * 12
SoWeekTonTaiTrenTheEarth = SoYearTonTaiTrenTheEarth * 48
SoDayTonTaiTrenTheEarth = SoYearTonTaiTrenTheEarth * 365
# Tính số tháng tuần ngày sống còn lại trên The Earth
SoMonthConSongTrenTheEarth = SoMonthTonTaiTrenTheEarth - (Tuoihientai * 12)
SoWeekConSongTrenTheEarth = SoWeekTonTaiTrenTheEarth - (Tuoihientai * 48)
SoDayConSongTrenTheEarth = SoDayTonTaiTrenTheEarth - (Tuoihientai * 365)
# Hiển thị kết quả
print("Thầy xin nhẹ nhàng thông báo với mày như sau:")
print(f"Mày chỉ còn tồn tại trên cái The Earth này {SoMonthConSongTrenTheEarth} tháng, {SoWeekConSongTrenTheEarth} tuần và {SoDayConSongTrenTheEarth} ngày nữa thôi.")

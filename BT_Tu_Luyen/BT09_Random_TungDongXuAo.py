"""
==========>>>>      Chương trình được tạo bởi Thầy Báo Viễn Thông --- PTIT_HCM      <<<<==========
----->  Viết chương trình tung đồng xu ảo, ngẫu nhiên cho người dùng biết "heads" hoặc "tails" (sấp hoặc ngửa)
"""

# Khai báo thư viện
import random
# Tạo hiệu ứng ngẫu nhiên
Rd = random.randint(1, 2)
if(Rd == 1):
    print("Heads")
if(Rd == 2):
    print("Tails")

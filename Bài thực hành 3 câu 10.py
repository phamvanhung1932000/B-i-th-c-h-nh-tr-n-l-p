# 10.

import math

R = float(input("Nhập R: "))  # nhập bán kính R từ bàn phím


def Tinh(R):
    if R < 0:  # R mà nhỏ hơn 0 thì không hợp lệ
        print("Bạn nhập không chính xác")
    else:
        Chu_vi = 2 * R * math.pi
        print("Chu vi là :", Chu_vi)
        Diện_tích = R * R * math.pi
        print("Diện tích là :", Diện_tích)


print("Kết quả phép tính")
Tính(R)
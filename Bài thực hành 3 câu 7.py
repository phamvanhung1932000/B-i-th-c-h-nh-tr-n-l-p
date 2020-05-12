#7.
def checkValue(n):
    #nhập vào số n, nếu chia hết cho 2 là số chẵn
    if n%2==0:                      # % có nghĩa là chia lấy phần dư
        print(" Đây là một số chẵn")
    #không chia hết cho 2 là số lẻ
    else:
        print(" Đây là một số lẻ")
#thay thử lần lượt các số khác nhau để kiểm tra thử
checkValue(10)

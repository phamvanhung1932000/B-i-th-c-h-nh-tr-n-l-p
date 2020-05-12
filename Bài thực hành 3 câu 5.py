# 5. Viết chương trình sau và xem sự thay đổi của biến
a = 'Hello Guy!'
def say():
    global a                    #global là biến toàn cục
    a = 'Vinh University'
    print(a)
say()
print(a)
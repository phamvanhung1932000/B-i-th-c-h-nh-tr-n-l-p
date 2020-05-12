#6
def get_sum(*num):
    tmp=0                   #khi tăng số lên thì kết quả cũng tăng lên
    # duyet cac tham so
    for i in num:
        tmp += i
    return tmp
result=get_sum(1,2,3,4,5)
print(result)

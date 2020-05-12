#9.

"""" Chương trình máy tính thực hiện các phép tính đơn giản """
#Nhập menu
print(" Chọn thao tác")
print("1.Thêm số vào")
print("2.Trừ số")
print("3.Nhân số")
print("4.Chia số")

# This function add two numbers( thêm hai số )
def add(x,y):
    return x+y
# This function subtracts two numbers ( trừ hai số )
def subtract(x,y):
    return x-y
# This function multiplies twon numbers ( nhân hai số )
def multiply(x,y):
    return x*y
# This function diviedes two numbers ( chia hai sô )
def divide(x,y):
    return x/y

# Chương trình chính
choice=input("Bạn muốn làm gì(1/2/3/4):")
num1=int(input("Nhập số đầu tiên:"))
num2=int(input("Nhập số thứ hai: "))

if choice=='1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Đầu vào không hợp lệ")
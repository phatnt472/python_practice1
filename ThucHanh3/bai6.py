a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
max,min = 0,0

if a > b: 
    max = a
    min = b
else:  
    max = b
    min = a
if c > max: 
    max = c
elif min > c: 
    min = c




print("Số lớn nhất và nhỏ nhất là: {max},{min}".format(max=max,min=min))
import math

xA = float(input("Nhập hoành độ diểm A: "))
yA = float(input("Nhập tung độ điểm A: "))

xB = float(input("Nhập hoành độ diểm B:"))
yB = float(input("Nhập tung độ điểm B:"))

xC = float(input("Nhập hoành độ diểm C: "))
yC = float(input("Nhập tung độ điểm C: "))

c = math.sqrt((xA - xB)**2 + (yA - yB)**2)
b = math.sqrt((xC - xA)**2 + (yC - yA)**2)
a = math.sqrt((xB - xC)**2 + (yB - yC)**2)

print(a,b,c)

if a + b > c and a + c > b and b + c > a:
    print("A,B,C có thể tạo thành tam giác!")

    if math.fabs(a**2 + b**2  -  c**2)  <= 0.000000001  or math.fabs(c**2 + a**2 -b**2) <= 0.000000001 or math.fabs(c**2 + b**2 - a**2) <= 0.000000001:
        print("ABC là tam giác vuông!")
    else:
        print("ABC không là tam giác vuông!")

    if a==b and b==c:
        print("ABC là tam giác đều!")
    else:
        print("ABC không là tam giác đều!")
else:
    print("A,B,C không thể tạo thành tam giác!")




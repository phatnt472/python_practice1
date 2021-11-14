a = int(input("Nhập hệ số a: "))
b = int(input("Nhập hệ số b: "))
c = int(input("Nhập hệ số c: "))
d = int(input("Nhập hệ số d: "))
e = int(input("Nhập hệ số e: "))
f = int(input("Nhập hệ số f: "))

D = a*e - b*d
Dx = c*e - b*f
Dy = a*f -d*c
print("Giải hệ pt: ")
print("{}x + {}y = {}".format(a,b,c))
print("{}x + {}y = {}".format(d,e,f))
if D != 0:
    print(f'Hệ pt có 2 nghiệm x = {Dx/D} , y = {Dy/D}')
elif Dx == 0 and Dy == 0 :
    print("Hệ pt có vô số nghiệm!")
else:
    print("Hệ pt vô nghiệm")




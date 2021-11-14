#Giải phương trình ax+b=0
a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))
if a == 0  and  b != 0:
    print(f"{a}x + {b} = 0 \nVô nghiệm")
elif a == 0 and b == 0:
    print(f'{a}x + {b} = 0 \nVô số nghiệm')
else:
    print(f'{a}x + {b} = 0\nx = {b/a*(-1)}')



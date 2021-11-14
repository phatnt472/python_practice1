import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a == 0:
     if b != 0:
         print(f'{b}x + {c} = 0 có nghiệm là {-c/b}')
     else:
        if c == 0:
            print(f'{b}x + {c} = 0 có vô số nghiệm')
        else:
            print(f'{b}x + {c} = 0 vô nghiệm')
            
else:
    delta =  b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2  = (-b - math.sqrt(delta))/(2*a)
        print(f'{a}x^2 + {b}x + {c} = 0 có hai nghiệm x1 ={x1}, x2 ={x2}')
    elif delta == 0:
        x = -b/(2*a)
        print(f'{a}x^2 + {b}x + {c} = 0 có nghiệm kép x = {x}')
    else:
        print(f'{a}x^2 + {b}x + {c} = 0 vô nghiệm')

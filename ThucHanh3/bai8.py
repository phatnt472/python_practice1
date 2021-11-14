import math
a  = float(input("Nhập cạnh thứ nhất: "))
b  = float(input("Nhập cạnh thứ hai: "))
c  = float(input("Nhập cạnh thứ ba: "))
laTamGiac = False
if a+b > c and a+c>b and b+c>a:
    laTamGiac = True
    print("ABC là tam giác!")
else:
   print("ABC không là tam giác!")

if laTamGiac == True:
    if a == b == c:
        print("ABC là tam giác đều!")
    else:
        print("ABC không là tam giác đều!")

    chuVi = a + b + c 
    nuaChuVi = chuVi/2
    dienTich = math.sqrt(nuaChuVi*(nuaChuVi-a)*(nuaChuVi-b)*(nuaChuVi-c))
    print("Chu vi :{}\nDiện tích {}".format(chuVi, dienTich))


import math
canh1=float(input("Nhập cạnh góc vuông thứ nhất: "))
canh2=float(input("Nhập cạnh góc vuông thứ hai: "))
canh3 = math.sqrt(canh1**2+canh2**2)
chuVi=canh1+canh2+canh3
nuaChuVi=chuVi/2
dienTich=math.sqrt(nuaChuVi*(nuaChuVi-canh1)*(nuaChuVi-canh2)*(nuaChuVi-canh3))
print(f"Chu vi: {chuVi}")
print(f"Diện tích: {dienTich}")

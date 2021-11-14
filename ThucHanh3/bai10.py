import random 

#khai báo các hằng số 
KEO = 0
BUA = 1
BAO = 2

#nhập lựa chọn của người
print("\n"*10)
print("Nhập lựa chọn của bạn")
print(f"Kéo: {KEO}")
print(f"Búa: {BUA}")
print(f"Bao: {BAO}")
nguoi = int(input("Nhập lựa chọn của bạn: "))

#tạo lựa chọn cho máy
may = random.randint(0,2)


if 0 <= nguoi <= 2:
    # in lựa chọn của người
    if nguoi == KEO:
        print("Bạn chọn kéo")
    elif nguoi == BUA:
        print("Bạn chọn búa")
    else:
        print("Bạn chọn bao")
   
   #in lựa chọn của máy
    if may == KEO:     
        print("Máy chọn kéo")
    elif may == BUA:
        print("Máy chọn búa")
    else:
        print("Máy chọn bao")
    
    #in kết quả
    if may == nguoi:
        print("Hoà nhau!")
    elif (may == KEO and nguoi == BAO)  or  (may == BAO and nguoi == BUA) or (may == BUA and nguoi == KEO):
        print("Máy thắng!")
    else:
        print("Bạn thắng!")
    
else:
    #in kết quả nếu chọn sai
    print("Bạn đã thua do chọn sai!")


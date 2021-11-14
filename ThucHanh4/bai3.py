doanhSo = int(input("Nhập vào doanh số: "))
if 0<doanhSo <=100:
    hueHong = 5/100
elif doanhSo <=300:
    hueHong = 10/100
else:
    hueHong = 20/100

tienHueHong = hueHong*doanhSo
print(f"Tiền huê hồng: {tienHueHong}")
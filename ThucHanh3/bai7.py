diemHe10 = float(input("Nhập điểm: "))
diemHe4 = 0
diemChu = ""

if 8.5 <= diemHe10 <= 10:
    diemHe4=4.0
    diemChu="A"
elif 7 <= diemHe10 < 8.5:
    diemHe4=3
    diemChu="B"
elif 5.5 <= diemHe10 < 7:
    diemHe4=2
    diemChu="C"
elif 4 <= diemHe10  < 5.5:
    diemHe4=1
    diemChu="D"
else:
    diemHe4=0
    diemChu="F"

print("Điểm hệ 10: {}\nĐiểm hệ 4: {}\nĐiểm chữ: {}\n".format(diemHe10,diemHe4,diemChu))
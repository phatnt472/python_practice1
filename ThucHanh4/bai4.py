cuocThueBao = 25000
phut = int(input("Nhập số phút: "))
tienCuoc = 0
if 0 <= phut <= 50:
    tienCuoc += 1000*phut
elif phut <= 200:
    tienCuoc += 1000*50 + 800*(phut - 50)
else:
    tienCuoc += 1000*50 + 800*150 + 300*(phut - 200)

print(f'Giá cước điện thoại của bạn là: {cuocThueBao + tienCuoc}')
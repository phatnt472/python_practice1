so_gio_cong = int(input("Nhập số giờ công: "))
so_gio_chuan = int(input("Nhập số giờ chuẩn: "))
don_gia = int(input("Nhập đơn giá theo giờ chuẩn: "))
so_gio_quy_doi = 0
if so_gio_chuan < so_gio_cong:
    so_gio_quy_doi = so_gio_chuan + (so_gio_cong - so_gio_chuan)*1.3
else:
    so_gio_quy_doi = so_gio_cong

tien_luong = don_gia * so_gio_quy_doi
print(f'Tiền lương tháng này là: {tien_luong}')
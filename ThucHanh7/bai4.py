str_ = input("Nhập vào 1 chuỗi: ")
print(f'Độ dài của chuỗi: {len(str_)}')
print(f'Kí tự đầu tiên của chuỗi: {str_[0]}')
print(f'Kí tự cuối cùng của chuỗi: {str_[-1]}')
print(f'3 kí tự đầu tiên của chuỗi: {str_[0:3]}')
print(f'3 kí tự cuối cùng của chuỗi: {str_[-3:None]}')
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
print(f"Chuỗi con từ vị trí {m} gồm {n} ký tự: {str_[m:m+n]}")



num = int(input("Nhập số nguyên: "))
string = ""
if num > 0:
    string = f"{num} là số dương!"
elif num == 0:
    string = f"{num} là số 0!"
else:
    string=f"{num} là số âm!"
print(string)
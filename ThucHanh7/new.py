import prettytable
class SinhVien:
  def __init__ (self,ten,diem):
    self.ten = ten
    self.diem = diem
  def printSV(self):
    print("Tên: ",self.ten)
    print("Điểm: ",self.diem)

num = 1
arr = []
for i in range(num):
  name = input("Nhập tên: ")
  score = float(input("Nhập điểm: "))
  sv = SinhVien(name,score)
  arr.append(sv)
x = PrettyTable()
x.field_names = ["Tên", "Điểm"]
for i in range(num):
  x.add_row(list(arr[i].ten,arr[i].diem))
print(x)
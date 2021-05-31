data_list = []

n = int(input('Menambahkan Angka List:'))
for m in range(0, n):
    data = str(int(input()))
    data_list.append(data)
print(data_list)
x = str(int(input('\n data input:')))
jumlah = data_list.count(x)
print("\n Banyaknya Angka '",x,"' adalah:", jumlah)
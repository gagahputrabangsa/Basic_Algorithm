angka_pertama = int(input('Masukkan bil pertama: '))
angka_kedua = int(input('Masukkan bil kedua: '))

#case 1
jumlah= angka_pertama+angka_kedua
print(jumlah)
#case 2
#1 angka kedua > angka pertama
if angka_kedua > angka_pertama:
    selisih = angka_kedua-angka_pertama
#2 angka pertama > angka kedua
else:
    selisih = angka_pertama - angka_kedua
print(selisih)














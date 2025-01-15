angka_pertama = int(input('Masukkan bil pertama: '))
angka_kedua = int(input('Masukkan bil kedua: '))

#case 1
jumlah= angka_pertama+angka_kedua
print(jumlah)
#case 2
#1 second num > first num
if angka_kedua > angka_pertama:
    selisih = angka_kedua-angka_pertama
#2 first num > second num
else:
    selisih = angka_pertama - angka_kedua
print(selisih)

#case 3 : multiply
perkalian = angka_pertama*angka_kedua 
print(perkalian)

#case 4: division
pembagian = angka_pertama/angka_kedua
print(pembagian)
#case 5: modulo
sisa_bagi = angka_pertama%angka_kedua
print(sisa_bagi)

#case 6: power = n1**n2
pangkat = angka_pertama**angka_kedua
print(pangkat)












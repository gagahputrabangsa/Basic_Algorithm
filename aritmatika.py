first_num = int(input('Masukkan bil pertama: '))
second_num = int(input('Masukkan bil kedua: '))

#case 1
jumlah= first_num+second_num
print(jumlah)
#case 2
#1 second num > first num
if second_num > first_num:
    selisih = second_num-first_num
#2 first num > second num
else:
    selisih = first_num - second_num
print(selisih)

#case 3 : multiply
perkalian = first_num*second_num 
print(perkalian)

#case 4: division
pembagian = first_num/second_num
print(pembagian)
#case 5: modulo
sisa_bagi = first_num%second_num
print(sisa_bagi)

#case 6: power = n1**n2
pangkat = first_num**second_num
print(pangkat)












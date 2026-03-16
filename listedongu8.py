
yukler=[10,14,12,23,20]

yeniDeger=[i*5 for i in yukler if i%2==1]
#yeniDeger=[i*5 for i in yukler if i>15]

for i in range(len(yeniDeger)):
    if(yeniDeger[i]%2==0):
        print("Yaz:",yeniDeger[i])

print("Sartli degerler:",yeniDeger)


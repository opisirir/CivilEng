
toplam=0
adet=int(input("Kac adet sayi girilecek?"))

for i in range(adet):
    print(f"{i+1}. sayiyi girin")
    sayi=int(input())
    toplam+=sayi

print("toplam:",toplam)


katyukler=[]
toplam=0

for i in range(5):
    katyukler.append(int(input(f"{i+1}.Kat yuk degeri giriniz:")))
    #toplam+=i
    toplam+=katyukler[i]

print("Toplam:",toplam)





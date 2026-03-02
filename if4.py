
yas=int(input("Yas giriniz:"))

if(yas<18):
    print("Cocuksunuz")
elif (yas>18 and yas<50):     #elif (yas>18 && yas<50): yazmaz
    print("Gencsiniz")
else:
    print("Yaslisiniz")



ad=input("Adiniz:")
v=float(input("Vize gir:"))
f=float(input("final gir"))

ort=(v*0.4)+(f*0.6)

if(ort>=60):
    print(f"{ad} Basarili ort:{ort}")
else:
    print("{} Basarisiz ort:".format(ad,ort))
    print(f"{ad} Basarisiz ort:{ort}")
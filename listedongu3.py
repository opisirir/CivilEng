
kolonkesit=[]
toplam=0

for i in range(5):
    kolonkesit.append(int(input(f"{i+1}.Kolon kesit gir:")))
    toplam+=kolonkesit[i]*4

print("toplam:",toplam)

for i in kolonkesit:
    if(i%2==0):
        print("Cift degerler:",i)

'''for i in range(5):
    if(i%2==0):
        print("Cift degerler:",i) '''
           

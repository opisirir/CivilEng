
import pandas as pd

veri={
    'Malzeme':['Celik','Ahsap','Plastik','Aluminyum'],
    'Maliyet':[500,620,410,200],
    'Dayanim':[8,6,4,5]
}

print(veri)
vericerceve=pd.DataFrame(veri)
print(vericerceve)

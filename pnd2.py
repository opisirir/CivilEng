import pandas as pd

veri={
    'Malzeme':['Celik','Ahsap','Plastik','Aluminyum'],
    'Maliyet':[500,620,40,200],
    'Dayanim':[8,6,4,5]
}

df=pd.DataFrame(veri)

print(df)

df.loc[df['Malzeme']=='Plastik','Maliyet']*=1.15

print(df)
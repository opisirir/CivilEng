import pandas as pd

veriler={
    'Numune':["N1","N2","N3"],
    'BetonSinif':["C20","C30","C30"],
    'dayanim':[25.6,28.7,31.8]
}

df=pd.DataFrame(veriler)

print(df)


riskliler=df[df['dayanim']<30]

print(riskliler)

riskliler.to_excel('analiz3.xlsx',index=False)

#openpyxl yüklü olmalı

df.to_csv('analiz2.csv',index=False)
import pandas as pd

df = pd.read_excel("beton_dayanim_sonuclari.xlsx")  #python dosyaniz ile ayni yerde mi?

print(df.head())
print(df.info())

dusuk_dayanim = df[df["Basinc_Dayanim"] < 30]  #exceldeki ile ayni mi?

ozet = df.groupby("Beton_Sinifi")["Basinc_Dayanim"].agg(
    ["mean", "min", "max", "std", "count"]
)

print("30 Mpa altindaki numuneler")
print(dusuk_dayanim)

print("Beton sinifina gore ozet:")
print(ozet)

ozet.to_excel("beton_ozet_analiz.xlsx")
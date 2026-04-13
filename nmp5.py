#Veri analizi

import numpy as np

veri=([12.4,17.5,25.3,20.4,22.9,8.4])
veri2=[12.4,17.5,25.3,20.4,22.9,8.4]

ort=np.mean(veri)
print(f"Ort:{ort:.2f}")
stdspma=np.std(veri)
print(f"std sapma:{stdspma:.2f}")
print(np.sum(veri2*5))

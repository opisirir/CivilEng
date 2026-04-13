import numpy as isim

isim.array([56,32,4])

print(isim.array([56,32,4]))

v1=isim.array([23,12,45])
print(v1)

m1=isim.array([ [2.2,5.3,6.7],[5.2,8.1,9.9]])

print(m1)

m2=isim.array([
[
    [4,6,8],
    [6,1,9],
    [8,6,7]
],
[
    [5,7,9],
    [4,9,10],
    [3,2,4]
]
])

print(m2)

print(v1.ndim) #boyut
print(m2.ndim)

print(m2.size) #eleman sayisi

print(m1.dtype)
print(v1.dtype)

print(m2.shape)
print(m1.shape)
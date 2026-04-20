import sympy as sp

x,y=sp.symbols('x y')

denk1=x+y-10
denk2=x-y+2

cozum=sp.solve((denk1,denk2),(x,y))

print(cozum)
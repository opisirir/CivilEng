import sympy as sp

x=sp.symbols('x')

expr=sp.sin(x)/x
limit_deger=sp.limit(expr,x,0)

print(limit_deger)




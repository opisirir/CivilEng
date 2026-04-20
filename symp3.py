import sympy as sp

x=sp.symbols('x')
q=2*x

V=sp.integrate(q,x)
M=sp.integrate(V,x)

print(V,M)
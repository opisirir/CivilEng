import sympy as sp

x=sp.symbols('x')

M=5*x**2-3*x
V=sp.diff(M,x)

print(V)
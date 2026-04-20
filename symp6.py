import sympy as sp

x=sp.symbols('x')
y=sp.Function('y')

denk=sp.Eq(sp.diff(y(x),x,4),x)

cozum=sp.solve(denk)
print(cozum)
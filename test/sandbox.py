from sympy import *
x, y = symbols('x y')

class sandbox:
    def __init__(self):
        gfg_exp = 3*(x**2) + x + 2*k*m
        coeffi1 = gfg_exp.coeff(x, 0)
        coeffi2 = gfg_exp.coeff(x, 1)
        coeffi3 = gfg_exp.coeff(x, 2)
        print(coeffi1, " ", coeffi2, " ", coeffi3, " ")


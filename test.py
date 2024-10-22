#Ceci est un test
def f(x):
    return x+1

def g(x):
    return f(f(x))

def phi(x):
    return x**3

def psi(x):
    return x**x

def P(L,x): #Transforme une liste de coefficients en polynome
    tot = 0
    for i in L:
        tot += x**i
    return tot 
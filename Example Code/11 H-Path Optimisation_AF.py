#E. McCarthy, A. Fragkou
def HOpt(F,dFx,dFy,x,y):
    import sympy as sym
    from sympy import symbols, solve
    import matplotlib.pyplot as plt

    hsym = symbols('hsym')

    xlist = []
    ylist = []
    flist = []
    dfxlist = []
    dfylist = []

    for i in range(0, 10, 1):
        xold = x
        yold = y

        dfx = dFx(x)
        dfy = dFy(y)

        #Create a function for the path to the top of the mountain.
        g = F(x+dfx*hsym, y+dfy*hsym)
        hexpr = sym.diff(g, hsym)

        hsolved = solve(hexpr)
        hopt = hsolved[0]

        x = xold + hopt*dfx
        y = yold + hopt*dfy

        Fxy = F(x, y)
        dfx = dFx(x)
        dfy = dFy(y)

        xlist.append(x)
        ylist.append(y)
        flist.append(Fxy)
        dfxlist.append(dfx)
        dfylist.append(dfy)

        if dfx <= 0.0001 and dfy <= 0.0001:
            break

    print(x, y, Fxy, dfx, dfy)

def F(x,y):
    return 2*x*y+2*x-x**2-2*y**2

def dFx(x):
    return 2*y+2-2*x

def dFy(y):
    return 2*x-4*y

x = 1.
y = 1.
print(HOpt(F, dFx, dFy, x, y))

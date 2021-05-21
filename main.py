from gradescent import *
from random import random

xp = [random() for _ in range(100)]
yp = [5 * x + 42 for x in xp]

def func1 (a, b):
    yyp = [a * x + b for x in xp]
    return sum((yy - y)**2 for yy,y in zip(yyp, yp))

xpar = Parameter("a", 2)
ypar = Parameter("b", integral=True, min=0, max=100, grid=10)
opt = Optimizer(func1, trace=True)
opt.add_par(xpar)
opt.add_par(ypar)
x = opt.optimize()
print ("optimum:", x)

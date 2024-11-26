import random as rand
from matplotlib import pyplot as pp

num = 500
n = 1000
X=[]
Y=[]
for i in range(num):
    x = [0]
    y = [0]
    step = [0]
    for j in range(n):
        x.append(x[-1]+rand.randint(-1,1))
        y.append(y[-1]+rand.randint(-1,1))
        step.append(j)
    X.extend([x[10],x[100],x[500],x[1000]])
    Y.extend([y[10],y[100],y[500],y[1000]])
    

    
pp.scatter(X,Y)
pp.xlim(-100,100)
pp.ylim(-100,100)
pp.show()
import numpy as np
from numpy.random import randn

np.set_printoptions(precision=2)

#Creating Arrays Using a List

a=np.array([1,2,3,4,5,6])
print(a)
b=np.array([[10,20,30],[40,50,60]])
print(b)

np.random.seed(25)
c1=np.random.randn(6)
print(c1)
c=36*np.random.randn(6)
print(c)

d=np.arange(1,35)
print(d)

print(a*10)

print(c+a)
print(c-a)
print(c*a)
print(c/a)
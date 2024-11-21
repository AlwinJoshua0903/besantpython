#what is called Zampda? - lamda are called as anonymous function means function without an name mostly used for single line operation
# lambda arguments-optional: expression

import math
c=lambda :"----------------------"
#without argument
l=lambda :"Helloworld"
print(l())
print(c())
# single argument
b=lambda d :d**2
print(b(27))
print(c())
#mutiple argument
m=lambda a=3,b=3:(a**2)+(2*a*b)+(b**2)
print(m(2,7))
print(c())
print(m(4,3))
print(c())
print(m(4))
print(c())
print(m(4,7))
print(c())
print(m())
print(c())

area_of_r=lambda r:math.pi*(r**2)
for d in range(0,11):
    print(f"Area of circle for radius{d}={area_of_r (d)}")




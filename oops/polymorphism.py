import math
#inbuild polymorphism
a=5
b=6
print(a+b)
a='hello'
b='world'
print(a+b)
#polymorphism with function
def add(x,y):
    return x*y
c=add(7,8)
print(c)
def sumno(*args):
    sum=0
    for a in args:
        sum+=a
    return sum
c=sumno(7,8)
print(c)
b=sumno(7,6,5)
print(b)
#class with polymorphism
class India():
    def population(self):
        print('India is my country')
    def type(self):
        print('devolping country')
class US():
    def population(self):
        print('US is my country')
    def type(self):
        print('devolped country')
class UAE():
    def population(self):
        print('UAE is my country')
    def type(self):
        print('devolping country')
'''i=India()
i.population()
i.type()
u=US()
u.population()
u.type()
e=UAE()   
e.population()
e.type()'''
i=India()
u=US()
e=UAE()
for a in (i,u,e):
    a.population()
    a.type()
#inheritance with polymorphism
class shape():
    def __init__(self):
        print("i am parent class for all")
    def volume(self):
        raise NotImplementedError("subclass must defined volume")
class square(shape):
    def __init__(self,a):
        self.a=a
    def volume(self):
        print(f"volume of square is{self.a*self.a}")
class circle(shape):
    def __init__(self,r):
        self.r=r
    def volume(self):
        print(f"volume of circle is{math.pi*(self.r**2)}")
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def volume(self):
        print(f"volume of rectangle is{self.l*self.b}")

x=square(5)
y=circle(6)
z=rectangle(3,4)
for p in (x,y,z):
    p.volume()
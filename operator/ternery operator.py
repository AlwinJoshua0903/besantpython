a=7
b=3
print("a is bigger" if a>b else "b is smaller")
print("a is bigger" if a<b else "b is smaller")

c=17
print ("Even" if c%2==0 else "Odd")
d=16
print ("Even" if d%2==0 else "Odd")

e=15
print("divisible by 2 and 3" if e%2==0 and e%3==0 else "divisible by 3")
print("divisible by 2 and 3" if e%2==0 or e%3==0 else "divisible by 3")

f=20
print("divisible by 2 and 3" if f%2==0 and f%3==0 else "divisible by 3" if f%3==0 else "not divisible by 3")
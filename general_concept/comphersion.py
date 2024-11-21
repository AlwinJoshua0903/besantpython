#comphersion
#converting multiple lines of code into single line
#always run faster than normal code
#comphersion type(list,dict,set)

L=[]
d={}
s=set()
for a in range(1,11):
    L.append(a**2)
    d[a]=a**2
    s.add(a**2)
print(s)
print(d)
print(L)
o=[a**2 for a in range(1,11)]
print(o)
d1={a:a**2 for a in range(1,11)}
print(d1)
s1={a**2 for a in range(1,11)}
print(s1)


li=[]
for a in range(1,15):
    if a%2:
        li.append(a)
print(li)
list=[a for a in range(1,15)if a%2]
print(list)
d=dict()
for a in range(1,15):
    if a%2:
        d[a]='odd'
print(d)

dicti={a:'odd' for a in range(1,15)if a%2}
print(dicti)

Listing=[]
for a in range(1,11):
    for b in range(1,11):
        Listing.append(a*b)
    print()
print(Listing)

liss=[a*b for a in range(1,11) for b in range(1,11)]
print(liss)

o=[]
for a in range(1,10):
    if a%2:
        o.append('odd')
    else:
        o.append('even')
print(o)

odd=['odd'if a%2 else 'even' for a in range(1,10)]
print(odd)

x1=dict()
for a in range(1,10):
    if a%2:
        x1[a]='odd'
    else:
        x1[a]='even'
print(x1)

even={a:'odd'if a%2 else 'even'for a in range(1,10)}
print(even)

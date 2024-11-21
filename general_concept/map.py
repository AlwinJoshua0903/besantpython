l=[1,4,2,9,10]
l1=lambda a: a**2
print(l1(2))
print(l1(9))
o1=list(map(l1,l))
print(o1)

num1=[4,5,10,12,13]
num2=[8,9,12,14,15]
l3=lambda a,b:(a**2)+(b**2)+(2*a*b)
o2=list(map(l3,num1,num2))
print(o2)

'''def tempcheck(t):
    o=[]
    temp=t
    for a in range(len(temp)):
        if temp[a]<0:
            o.append('cold')
        elif temp[a]>=0 and temp[a]<=15:
            o.append('medium cold')
        elif temp[a]>=16 and temp[a]<=25:
            o.append('medium hot')
        elif temp[a]>=26 and temp[a]<=30:
            o.append('hot')
        else:
            o.append('extreme hot')
    return o
''''''tempv=tempcheck([11,8,4,2,14,25,37,-8,-4])
print(tempv)'''
'''o3=list(map(tempcheck,[11,8,4,2,14,25,37,-8,-4]))
print(o3)'''

def tempcheck_single(temp):
    o=[]
    if temp < 0:
        o.append('cold')
    elif temp >= 0 and temp <= 15:
        o.append('medium cold')
    elif temp >= 16 and temp <= 25:
        o.append('medium hot')
    elif temp >= 26 and temp <= 30:
        o.append('hot')
    else:
        o.append('extreme hot')
    return o
input=[11, 8, 4, 2, 14, 25, 37, -8, -4]
o3 = list(map(tempcheck_single,input))
print(o3)
zippedoutput=dict(zip(input,o3))
print(zippedoutput)

def sumof(n):
    sum=0
    for a in str(n):
        sum+=int(a)
    return sum
#o=sumof(487)
#print(o)
m=[234,6778,4556]
output=list(map(sumof,m))
print(output)
combined=dict(zip(m,output))
print(combined)

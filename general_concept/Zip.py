#matchable will be printed
'''L=[1,2,3,4,5,6,7]
L1=['A','B','C','d','e','f','g']
print(L)
print(L1)
x=zip(L,L1)
print(x)
print(list(x))
print(dict(x))
print(set(x))'''

#dictionary- cannot zip the more than 2 elements
day=[0,1,2,3,4,5,6]
dayname=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
wd=[1,2,3,4,5,6,7]
x=list(zip(day,dayname,wd))
print(x)
'''print(dict(x))
print(set(x))'''

'''day=[0,1,2,3,4,5,6]
dayname=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
x=list(zip(day,dayname))
print(x)
print(dict(x))
print(set(x)'''

#Unzip

statepincode=[('Knagar',600001),('Anagar',600002),('Cnagar',600003)]
print(statepincode)
state,pincode=zip(* statepincode)
print(state)
print(pincode)
day,dayname,wd=zip(* x)
print(day)
print(dayname)
print(wd)
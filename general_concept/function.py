#def-keyword function name (arguments)
#lambda to function possible, function to lambda not possible
#without argument
'''def Hello():
    print("Welcome to function")
Hello()

def Hello1():
    return "Helloworld"
a=Hello1()
print(a)
#with Arguments
def addition2(num1,num2):
    return num1+num2
b=addition2(6,5)
print(b)

def Arithmeticoperation(symbol,num3,num4):
    if symbol in['//','**','%']:
        return ("invalid operation")
    else:
        if symbol=='+':
            return f"addition of {num3} and {num4} = {num3+num4}"
        elif symbol=='-':
            return f"subtraction of {num3} and {num4} = {num3-num4}"
        elif symbol=='*':
            return f"multiplication of {num3} and {num4} = {num3*num4}"
        else:
            return f"subtraction of {num3} and {num4} = {num3/num4}"
symble=input("Enter the Symbol :")
num5=int(input("Enter the number :"))
num6=int(input("Enter the number :"))
b=Arithmeticoperation(symble,num5,num6)
print(b)'''

#Non key arguments
#*args
'''def sum(*nums):
    sum=0
    for a in nums:
        sum/=a
    return sum
d=sum(1)
e=sum(10,14,10)
print(d)
print(e)'''
def strings(*word):
    sum=""
    for a in word:
        sum+=a
        sum+="-"
    return sum
f=strings("Hello","world")
print(f)
def strings(*word):
    sum=""
    for a in word:
        sum+=a
        sum+="-"
    return sum
f=strings("Hello","world")
print(f)

def str1(*words):
    output=" "
    h=1
    for a in words:
        output+=a
        if h==1:
            temp="-"*h
            output+=temp
            h+=1
        else:
            temp = "-"*h
            output+= temp
            h+=1
    return output
i=str1("Hello","world","welcome")
print(i)

#keyword arguments-keyvaluepairs
def printmessage(**args):
    for a in args:
        print(a,args[a])
printmessage(id=1,name='ruban')




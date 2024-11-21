#diff while vs for?
#Iterative loop
#For - Endpoint should know first. Example travel for first 100km.
#while - until the condition get satisfy. Example travel until destination is reached.
#For to while conversion possible,while to for conversion not possible.
#simple program
'''i=1
while(i<=10):
    print(i)
    i+=1'''
#for ro while conversion
'''a=1
while(a<=9):
    b=1
    while(b<=9):
        print(a*b,end=" ")
        b+=1
    print()
    a+=1
a=1
while(a<=5):
    b=1
    while(b<a+1):
        print(b,end=" ")
        b+=1
    print()
    a+=1'''
from for_ import *
flag=True
while(flag):
    n=int(input("Enter the number to guess :"))
    if n==numbertoguess:
        print("you have identified number correctly")
        flag=False
    elif n<numbertoguess:
        print("you have entered smaller number")
    else:
        print("you have entered bigger number")





#Armstrong number
'''n=int(input("Enter the Armstrong Number :"))
sumofdigit=0
for a in str(n):
    sumofdigit+=int(a)**(len(str(n)))
if n==sumofdigit:
    print("Is an Armstrong number")
else:
    print("Is not an Armstrong number")'''

#palindrome
'''a=input("Enter the string to check :")
print(a)
reversestring=(a[::-1])
if a==reversestring:
    print("It is a palindrome")
else:
    print("It is not a palindrome")'''

'''a=int(input("Enter the number :"))
sumofdigit=0
for x in str(a):
    sumofdigit+=int(x)
print(sumofdigit)'''

a=int(input("Enter the number :"))
if a>1:
    for i in range(2,(a//2)+1):
        if(a%i)==0:
            print(a,"It's not a prime number")
            break
    else:
        print(a,"It's a prime number")
else:
    print(a,"It's not a prime number")

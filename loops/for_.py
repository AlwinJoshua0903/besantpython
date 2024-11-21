#End point
#syntax:
# for a-variable in range(10-endpoint):
# for a-variable in range(1-startpoint,10-endpoint):
# for a-variable in range(1-startpoint,10-endpoint,2-step):
'''for a in range(15):
    print(a)
for a in range(1,14):
    print(a)
for a in range(1,11,2):
    print(a)'''
'''for  a in "hello":
    print(a)
for a in [1,2,4,9,1]:
    print(a+2)'''
'''d=dict()
s=set()
ol=[]
for a in range(1,11):
    ol.append(a**2)
    s.add(a**2)
    d[a]=a**2
print(d)
print(s)
print(ol)'''


'''
for a in range(5):
    username = input("enter the username:")
    password = input("enter the username:")
    if username == "Admin" and password == "Admin":
        print("successful login")
    elif username == "Admin" and password != "Admin":
        print("incorrect Password")
    elif username != "Admin" and password == "Admin":
        print("incorrect username")
    else:
        print("Both are not correct")
'''

'''for a in range(10):
    print(a,end=" ")
print()
print("hello")'''

#nested for

'''for a in range(1,15):
    for b in range(1,20):
        print(f'{a}*{b}={a*b}',end=" ")
    print()'''

'''for a in range(1,6):
    for b in range(1,a+1):
        print('*',end=" ")
        #print(a*b,end=" ")
        #print(a,end=" ")
        #print(b,end=" ")
    print()'''

'''starting_value=1
for a in range(1,6):
    for b in range(1,a+1):
        if a%2==1:
            print('*',end=" ")
            starting_value += 1
        else:
            print(starting_value,end=" ")
            starting_value+=1
    print()'''


# for a in range(1,8):
#     if a==4:
#         for b in range(1,5):
#             print('*',end=" ")
#         print()
#     else:
#         for b in range(1, 5):
#             if b in (1,4):
#                 print('*',end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
#Y
'''for a in range(1,7):
    if a in[1,2]:
        for b in range(1,6):
            if b in[1,5]:
                print('*',end=" ")
            else:
                print(" ",end=" ")
        print()
    elif a in [3]:
        for b in range(1, 6):
            if b in [2,4]:
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print()
    else:
        for b in range(1, 6):
            if b==3:
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print()'''


#x
'''for a in range(1,6):
    if a in[1,5]:
        for b in range(1,6):
            if b in[1,5]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    elif a in [2,4]:
        for b in range(1, 6):
            if b in [2,4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    else:
        for b in range(1,6):
            if b==3:
                print("*",end=" ")
            else:
                print(" ", end=" ")
        print()'''
#O
'''for a in range(1,5):
    if a in[1,4]:
        for b in range(1,6):
            if b in[2,3,4]:
                print('*',end=" ")
            else:
                print(" ",end=" ")
        print()
    else:
        for b in range(1,6):
            if b in[1,5]:
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print()'''
'''#M
for a in range(1,6):
    if a in[1,4,5]:
        for b in range(1,6):
            if b in[1,5]:
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print()
    elif a in [1,2,4,5]:
        for b in range(1, 6):
            if b in [1,2,4,5]:
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print()
    else:
        for b in range(1,6):
            if b in[1,3,5]:
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print()'''
'''for a in range(1,6):
    if a in[2,4,5]:
        for b in range(1,6):
            if b in[1]:
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print()
 #   elif a in [1,3]:
    else:
        for b in range(1, 6):
            if b in [1,2,3,4,5]:
                print('*', end=" ")
            else:
                print(" ", end=" ")
        print()

for a in range(1,5):
    if a in[1,4]:
        for b in range(1,6):
            if b in[1,5]:
                print('w', end=" ")
            else:
                print(" ", end=" ")
        print()
    elif a in[3]:
        for b in range(1,6):
            if b in [1,2,4,5]:
                print('w', end=" ")
            else:
                print(" ", end=" ")
        print()
    elif a in[2]:
        for b in range(1,6):
            if b in[1,3,5]:
                print('w', end=" ")
            else:
                print(" ", end=" ")
        print()'''
numbertoguess=77


















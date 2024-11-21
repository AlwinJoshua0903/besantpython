#condition loop
'''num=int(input("enter the value:"))
if num<=10:
    print("below 10 or 10")
elif num<=100:
    print("below 100 or 100")
elif num<=1000:
    print("below 1000 or 1000")
else:
    print("above 1000")'''
'''id=int(input("enter the id:"))
name=input("enter the name:")
m1=int(input("enter the m1:"))
m2=int(input("enter the m2:"))
m3=int(input("enter the m3:"))
total=m1+m2+m3
avg=total/3
print(f"total of {name}={total}")
print(f"average of {name}={avg}")
if total>290:
    print("grade A+")
elif total<290 and total>=275:
    print("grade A")
elif total<275 and total>=250:
    print("grade B")
elif total<250 and total>=200:
    print("grade c")
else:
    print("grade D")


if m1<35 or m2<35 or m3<35:
    if m1<35 and m2<35 and m3<35:
        print("failed in all sub")
    elif m1<35 and m2<35:
        print("failed in 1 & 2")
    elif m2<35 and m3<35:
        print("failed in 2 & 3")
    elif m3<35 and m1<35:
        print("failed in 3 & 1")
    elif m1<35:
        print("failed in 1")
    elif m2< 35:
        print("failed in 2")
    else:
        print("failed in 3")
else:
    total = m1 + m2 + m3
    avg = total / 3
    print(f"total of {name}={total}")
    print(f"average of {name}={avg}")
    if total >=290:
        print("Grade A+")
    elif total < 290 and total >= 275:
        print("grade A")
    elif total < 275 and total >= 250:
        print("grade B")
    elif total < 250 and total >= 200:
        print("grade C")
    else:
        print("grade D")'''
username=input("enter the username:")
password=input("enter the username:")
if username == "Admin" and password == "Admin":
    print("successful login")
elif username == "Admin" and password != "Admin":
    print("incorrect Password")
elif username != "Admin" and password == "Admin":
    print("incorrect username")
else:
    print("Both are not correct")



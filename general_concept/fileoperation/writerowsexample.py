import csv
import os
fileexist=os.path.isfile('studentmultiple.csv')
print(fileexist)
n=int(input('Enter the number of student: '))
studentlist=[]
for a in range(n):
    tempst=[]
    id = int(input("student_id"))
    name = input("enter the name")
    Mark1 = int(input("enter mark1"))
    Mark2 = int(input("enter mark2"))
    Mark3 = int(input("enter mark3"))
    total = Mark1 + Mark2 + Mark3
    Avg = total / 3
    if total >= 290:
        grade = 'a'
    elif total < 290 and total >= 275:
        grade = 'b'
    elif total < 275 and total >= 250:
        grade = 'c'
    elif total < 250 and total >= 200:
        grade = 'd'
    else:
        grade = 'e'
    tempst.append(id)
    tempst.append(name)
    tempst.append(Mark1)
    tempst.append(Mark2)
    tempst.append(Mark3)
    tempst.append(total)
    tempst.append(Avg)
    tempst.append(grade)
    studentlist.append(tempst)
    print(studentlist)
with open('studentmultiple.csv','a',newline='')as file:
    if fileexist:
        writer=csv.writer(file)
        #writer.writerow(['id','name','Mark1','Mark2','Mark3','total','Avg','grade'])
        writer.writerows(studentlist)
    else:
        writer=csv.writer(file)
        writer.writerow(['id','name','Mark1','Mark2','Mark3','total','Avg','grade'])
        writer.writerows(studentlist)

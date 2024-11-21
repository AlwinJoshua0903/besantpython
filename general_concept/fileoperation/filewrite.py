#file modes-write,append,read
#write
import csv
import os
fileexist=os.path.isfile('studentout.csv')
print(fileexist)
id=int(input("student_id"))
name= input("enter the name")
Mark1=int(input("enter mark1"))
Mark2=int(input("enter mark2"))
Mark3= int(input("enter mark3"))
total = Mark1+Mark2+Mark3
Avg=total/3
if total>=290:
    grade='a'
elif total <290 and total>=275:
    grade='b'
elif total<275 and total>=250:
    grade='c'
elif total<250 and total>=200:
    grade='d'
else:
    grade='e'
print(id,name,Mark1,Mark2,Mark3,total,Avg,grade)
with open('studentout.csv','a',newline='')as file:
    if fileexist:
        writer=csv.writer(file)
        #writer.writerow(['id','name','Mark1','Mark2','Mark3','total','Avg','grade'])
        writer.writerow([id,name,Mark1,Mark2,Mark3,total,Avg,grade])
    else:
        writer=csv.writer(file)
        writer.writerow(['id','name','Mark1','Mark2','Mark3','total','Avg','grade'])
        writer.writerow([id,name,Mark1,Mark2,Mark3,total,Avg,grade])


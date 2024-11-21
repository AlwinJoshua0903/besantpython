'''id=int(input("Enter the Student ID:"))
name=input("Enter the Name:")
Mark1=int(input("Enter the Mark1:"))
Mark2=int(input("Enter the Mark1:"))
Mark3=int(input("Enter the Mark1:"))
total=Mark1+Mark2+Mark3
Avg=total/3
if total>=290:
    grade='a'
elif total<290 and total<=275:
    grade='b'
elif total<275 and total<=250:
    grade='b'
elif total<250 and total<=200:
    grade='b'
else:
    grade='e'
print(total)
print(Avg)
print(grade)
print(f"insert into student_python values({id},'{name}',{Mark1},{Mark2},{Mark3},{total},{Avg},'{grade}')")'''

import mysql.connector
config = {
    'user': 'root',
    'password': 'Alwinbhavi@0903',
    'host': 'localhost',
    'database': 'besant'
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

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

mysql=f"insert into studentpython values({id},'{name}',{Mark1},{Mark2},{Mark3},{total},{Avg},'{grade}')"
cursor.execute(mysql)

cnx.commit()
# close
cursor.close()

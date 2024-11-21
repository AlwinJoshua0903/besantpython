import mysql.connector
config = {
    'user': 'root',
    'password': 'Alwinbhavi@0903',
    'host': 'localhost',
    'database': 'besant'
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def readallstudent():
    sql="select * from studentpython"
    cursor.execute(sql)
    output=cursor.fetchall()
    for a in output:
        print(a)
#readallstudent()

#value=int(input("Enter the value for id : "))
def readsinglestudent(id):
    sql=f"select * from studentpython where id={id}"
    cursor.execute(sql)
    output = cursor.fetchall()
    for a in output:
        print(a)
#readsinglestudent(value)

'''valued=int(input("Enter the value for id : "))
'''
def deletestudent(id):
    sql=f"delete from studentpython where id={id}"
    cursor.execute(sql)
    cnx.commit()
    cursor.close()
#deletestudent(3)
def insertstudent(id,name,mark1,mark2,mark3,gender,Dob,location,coursetaken):
    total = mark1 + mark2 + mark3
    average = total / 3
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
    mysql=f"insert into studentpython values({id},'{name}',{mark1},{mark2},{mark3},{total},{average},'{grade}','{gender}','{Dob}','{location}','{coursetaken}')"
    cursor.execute(mysql)
    cnx.commit()
'''id=int(input("student_id"))
name= input("enter the name")
Mark1=int(input("enter mark1"))
Mark2=int(input("enter mark2"))
Mark3= int(input("enter mark3"))
total = Mark1+Mark2+Mark3'''

#update
def updatestuendt(id,name,mark1,mark2,mark3):

    total = mark1 + mark2 + mark3
    average = total / 3
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
    mysql = f"update studentpython set name='{name}',Mark1={Mark1} where id={id}"
    cursor.execute(mysql)  # it is  used to insert,delete,update....
    cnx.commit()  # it is  used to insert,delete,update....
'''id=int(input("student_id"))
name= input("enter the name")
Mark1=int(input("enter mark1"))
Mark2=int(input("enter mark2"))
Mark3= int(input("enter mark3"))'''

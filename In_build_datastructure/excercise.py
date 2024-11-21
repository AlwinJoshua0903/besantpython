L1=[1,4,2,3,7]
L2=[4,2,19,7,1]
#find the unique values among both list
s1=set(L1)
s2=set(L2)
s3=list(s1.union(s2))
print(s3)
#interchange the element in the list
L3=[[1,2,3,4],[7,8,9,10],[11,12,13,14]]
print(L3)
print(L3[1])
print(L3[2][2])
a=L3[0][1]
b=L3[0][2]
c=a
L3[0][1]=b
L3[0][2]=c
print(L3)
a=L3[1][1]
b=L3[1][2]
c=a
L3[1][1]=b
L3[1][2]=c
print(L3)
a=L3[2][1]
b=L3[2][2]
c=a
L3[2][1]=b
L3[2][2]=c
print(L3)
#change the value of the element in the list
L3[1][3]=100
print(L3)
#append
L3[1].append(121)
print(L3)
L3.append([21,22,23,24])
print(L3)
#append vs insert vs extend
student={'Id':1,'name':'xyz','phone':9740203050,'location':'chennai',
'course_taken':{'course_no1':1,'course_name1':'python',
                'course_no2':2,'course_name2':'aws',
                'course_no3':3,'course_name3':'devops','status':'completed'}}
student['course_taken']['course_name1']='DJango'
print(student)
student['course_taken']['course_no4']='4'
student['course_taken']['course_name4']='Python'
print(student)
l4=[2,3,4,5]
l5=[3,4,5,6]
print(l4+l5)
print(l4*5)
s5={1,2,3,4}
s6={3,4,5,6}
#print(s5+s6)(not working)

L7=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(L7)
print(L7[1])
print(L7[-4])
print(L7[:])
print(L7[2:])
print(L7[:5])
print(L7[0:8])
print(L7[0:8:2])
print(L7[0:8:3])
print(L7)
print(L7[::-1])
L7.sort()
print(L7)
L7.sort(reverse=True)
print(L7)


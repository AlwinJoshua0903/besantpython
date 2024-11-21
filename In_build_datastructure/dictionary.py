#always keys with same name in these Means it will print only latest key
#Keyvaluepairs

aadhar={'name':'Alwin','phone':9723456790,'phone1':9723456780,'name':'joshua'}
print(aadhar)
print(dir(aadhar))
aadhar1=aadhar.copy()
print(aadhar1)
aadhar1.clear()
print(aadhar1)
print(aadhar.keys())
print(aadhar.values())
print(aadhar.items())

student={'Id':1,'name':'xyz','phone':9740203050,'location':'chennai',
'course_taken':{'course_no1':1,'course_name1':'python',
                'course_no2':2,'course_name2':'aws',
                'course_no3':3,'course_name3':'devops','status':'completed'}}
#nested dictionary
print(student)
print(student['course_taken'])
print(student['course_taken']['course_name1'])
print(student['course_taken']['status'])
#get
print(student.get('name'))
#popitem(last value deleted)
print(student)
student.popitem()
print(student)
student.pop('phone')
print(student)
#adding key value in dictionary
student['phone']=9720304050
print(student)
student['course_taken']={'course_no1':1,'course_name1':'python',
                'course_no2':2,'course_name2':'aws',
                'course_no3':3,'course_name3':'devops','status':'completed'}
print(student)
#from keys
a=['a','e','i','o','u']
v=0
o=dict.fromkeys(a,v)
print(o)
d3={'Id':1,'name':'xyz','salary':20000}
d4={'Id':1,'name':'xyz1','salary':20000,'phone':9234567890,'location':'madurai'}
#update
d3.update(d4)
print(d3)
#set-Default
d4.setdefault('location','chennai')
print(d4)

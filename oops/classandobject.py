#class-blue print
#important question-how to create a empty class
#without obj cannot access the member function
class a:
    pass
#if there is print statement inside class it will print all those
class b:
    print("All are welcome")
    print("All are present")
    c=10
    print(c)

class class1:
    training='Tam'
    course='python'
    def welcometooops(self):
        print('hi')
a=class1()
print(a.training)
print(a.course)
a.welcometooops()
print(class1.training)


class Employee:
    company = 'Tutorial Gateway'

    def func_message(self):
        print('Welcome to Programming')


emp = Employee()
print(emp.company)
emp.func_message()

print("-------------")
print(Employee.company)
emp.func_message()

#__init__ -constructor
#It has 2 types-parameterized,non parameterized
#__init__ run when object is created

#Nonparamterized constructor
class Employee:
    company = 'Tutorial Gateway'

    def __init__(self):
        print('Hello World')

    def func_message(self):
        print('Welcome to Python Programming')


emp1 = Employee()  # Created an Instance

print(emp1.company)
emp1.func_message()

#Paramterized Constructor
class Employee:
    company = 'Tutorial Gateway'

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def func_message(self):
        print('Welcome to Programming')

    def printmsg(self):
        print(f"{self.name},welcome to oops class and is age was={self.age}and gender={self.gender}")


emp1 = Employee('Jack', 25, 'Male')
emp2 =Employee('alwin',22,'Male')
print(emp1.company)
emp1.func_message()
emp1.printmsg()
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp2.printmsg()
emp2.name='Msd'
emp2.printmsg()



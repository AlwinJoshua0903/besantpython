#decorator classmethod
class Employee:
    company = 'Tutorial Gateway'

    @classmethod
    def message(cls):
        print('The Message is From %s' % cls.__name__)
        print('The Company Name is %s' % cls.company)


Employee.message()

print('-----------')
Employee().message()  # Other way of calling

#function class method
class Employee:
    value = 100

    def printValue(cls):
        print('The Value = %d' % cls.value)


Employee.printValue = classmethod(Employee.printValue)
Employee.printValue()

#staticmethod
class Employee:
    company = 'Tutorial Gateway'

    @classmethod
    def message(cls):
        print('The Company Name is %s' % cls.company)
        print('The Message is From %s Class' % cls.__name__)
        cls.func_msg()

    @staticmethod
    def func_msg():
        print("Welcome to Python Programming")
Employee.message()


class Employee:
    company = 'Tutorial Gateway'

    @staticmethod
    def add(a, b, c):
        return a + b + c

    @classmethod
    def avg(cls):
        x = cls.add(10, 20, 40)
        return (x / 3)


average = Employee.avg()
print('The Average Of three Numbers = ', average)


class Employee:
    company = 'Tutorial Gateway'

    @classmethod
    def func_newName(cls, new_Name):
        cls.company = new_Name


emp = Employee()

print(Employee.company)
print(emp.company)

print('----------')
Employee.func_newName('Coding')

print(Employee.company)
print(emp.company)


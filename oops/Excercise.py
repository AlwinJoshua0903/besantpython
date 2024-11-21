class header:
    def __init__(self):
        print("""
        --------------------------------------------------
        -------------welcome to Electric Board------------
        --------------------------------------------------
        """)
class footer:
    def __init__(self):
        print("""
            --------------------------------------------------
            ---------------------Thank You--------------------
            ---------------------Visit Again------------------
            """)
class billcal:
    def __init__(self,unit):
        self.unit=unit
    def billscal(self):
        print(f"number of units consumed={self.unit}")
        if self.unit<=100:
            charges=0.0
        elif self.unit<=200:
            charges=(100*0)+((self.unit-100)*2.25)
        elif self.unit<=400:
            charges=(100*0)+((self.unit-100)*2.25)+((self.unit-200)*4.50)
        elif self.unit<=500:
            charges=(100*0)+((self.unit-100)*2.25)+((self.unit-200)*4.50)((self.unit-100)*6.0)
        else:
            charges=(100*0)+((self.unit-100)*2.25)+(200*4.5)+(100*6.0)+((self.unit-100)*8.0)
        print(f"Bill amount= {charges}")


u=int(input("Enter the no of units:"))
h=header()
b=billcal(u)
b.billscal()
f=footer()


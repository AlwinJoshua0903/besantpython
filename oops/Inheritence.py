#single inheritance

'''class father():
    def __init__(self,fname,fage,flocation):
        self.fname=fname
        self.fage=fage
        self.flocation=flocation
    def printfather(self):
        return f"Fathername {self.fname}and is age {self.fage}and is from {self.flocation}"

class son(father):
    def __init__(self,fname,fage,flocation,sname,sage,slocation):
        father.__init__(self,fname,fage,flocation)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"Sonname {self.sname} and is age {self.sage} and is from {self.slocation}"

s1=son('Raja','55','kovilpatti','Alwin','22','kovilpatti')
o1=s1.printfather()
o2=s1.printson()
print(o1)
print(o2)'''

#multilevel
'''class grandfather():
    def __init__(self,gname,gage,glocation):
        self.gname=gname
        self.gage=gage
        self.glocation=glocation
    def printgrandfather(self):
        return f"GrandFathername {self.gname}and is age {self.gage}and is from {self.glocation}"
class father(grandfather):
    def __init__(self,fname,fage,flocation,gname, gage, glocation):
        grandfather.__init__(self, gname, gage, glocation)
        self.fname=fname
        self.fage=fage
        self.flocation=flocation
    def printfather(self):
        return f"Fathername {self.fname}and is age {self.fage}and is from {self.flocation}"

class son(father):
    def __init__(self,gname,gage,glocation,fname,fage,flocation,sname,sage,slocation):
        father.__init__(self,gname,gage,glocation,fname,fage,flocation)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"Sonname {self.sname} and is age {self.sage} and is from {self.slocation}"
s1=son('Raja','55','kovilpatti','Alwin','40','kovilpatti','josh','22','kovilpatti')
o=s1.printgrandfather()
o1=s1.printfather()
o2=s1.printson()
print(o)
print(o1)
print(o2)'''

#multiple

'''class mother():
    def __init__(self,mname,mage,mlocation):
        self.mname=mname
        self.mage=mage
        self.mlocation=mlocation
    def printmother(self):
        return f"Mothername {self.mname}and is age {self.mage}and is from {self.mlocation}"
class father():
    def __init__(self,fname,fage,flocation):
        self.fname=fname
        self.fage=fage
        self.flocation=flocation
    def printfather(self):
        return f"Fathername {self.fname}and is age {self.fage}and is from {self.flocation}"

class son(father,mother):
    def __init__(self,mname,mage,mlocation,fname,fage,flocation,sname,sage,slocation):
        mother.__init__(self,mname,mage,mlocation)
        father.__init__(self,fname,fage,flocation)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"Sonname {self.sname} and is age {self.sage} and is from {self.slocation}"

a1=son('Raja','55','kovilpatti','Alwin','40','kovilpatti','josh','22','kovilpatti')
a2=a1.printmother()
a3=a1.printfather()
a4=a1.printson()
print(a2)
print(a3)
print(a4)'''

#hierarchical

'''class family():
    def __init__(self,famname,surname,origin):
        self.famname=famname
        self.surname=surname
        self.origin=origin
    def printfamily(self):
        return f"Familyname {self.famname}and surname is {self.surname}and origin from {self.origin}"
class son(family):
    def __init__(self,famname,surname,origin,sname,sage,slocation):
        family.__init__(self,famname,surname,origin)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"Sonname {self.sname} and is age {self.sage} and is from {self.slocation}"
class son1(family):
    def __init__(self,famname,surname,origin,sname,sage,slocation):
        family.__init__(self,famname,surname,origin)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"Son1name {self.sname} and is age {self.sage} and is from {self.slocation}"
class son2(family):
    def __init__(self,famname,surname,origin,sname,sage,slocation):
        family.__init__(self,famname,surname,origin)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"Son2name {self.sname} and is age {self.sage} and is from {self.slocation}"
a1=son('Raja','XYZ','kovilpatti','Alwin','40','kovilpatti')
a2=a1.printfamily()
a4=a1.printson()
print(a2)
print(a4)
b1=son1('Mano','XYZ','kovilpatti','Josh','40','kovilpatti')
b2=b1.printfamily()
b3=b1.printson()
print(b2)
print(b3)
c1=son2('Fam','XYZ','kovilpatti','Shiva','40','kovilpatti')
c2=c1.printfamily()
c3=c1.printson()
print(c2)
print(c3)'''

#hybrid


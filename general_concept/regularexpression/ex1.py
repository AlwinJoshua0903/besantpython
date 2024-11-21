import re
'''text="hello world"
print(text)
n=re.findall('z',text)
print(n)
if len(n)==0:
    print("letter is not present in string")
else:
    print(f"letter is present number of times={len(n)}")'''

'''text1="i will wake by 7 and start the class by 8"
nofn=re.findall("[0-9]",text1)
print(nofn)
v=len(nofn)
print(v)
phone="6783323456"
validph=re.findall("[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",phone)
print(validph)
if len(validph)==0:
    print("Invalid PhoneNUmber")
else:
    print("Valid PhoneNumber")

time="23:45"
validtime=re.findall("[0-2][0-9]:[0-6][0-9]",time)
print(validtime)
if len(validtime)==0:
    print("Invalid PhoneNUmber")
else:
    print("Valid PhoneNumber")
a="hello Hello 0 Python py 1 Welcome we 2"
numberofsmallletter=re.findall("[a-z]",a)
numberofcapsletter=re.findall("[A-Z]",a)
print(numberofsmallletter)
print(numberofcapsletter)
bothcapsmallalphabet=re.findall("[a-z]|[A-Z]",a)
print(bothcapsmallalphabet)'''

'''txt="welocme to my programming world"
print(txt)
numberofwords=re.split(" ",txt)
print(numberofwords)

txt1="welocme to my programming world"
print(txt1)
numberofsplitwords=re.split("o",txt1)
print(numberofsplitwords)

texting="raining in spain"
print(texting)
firstspace=re.search("i",texting)
print(firstspace)
print(firstspace.start()
p='welcome to my world'
numberofsplit=re.split(' ',p,1)
print(numberofsplit)
s='box is bigger and heavier'
print(s)
replaceds=re.sub("box","fox",s)
print(replaceds)
r=re.sub(" ","9",s,2)
print(r)
t="Welcome to Regular Expressionrrr in python"
print(t)
x=re.search(r"\bE\w+",t)
print(x.span())
print(x.string)
print(x.group())

#(^-starting,$-ending for sentence)
startingcheck=re.search("^Welcome",t)
print(startingcheck)
endingcheck=re.search("Welcome.*python$",t)
print(endingcheck)'''

'''st="hello world"
output=re.findall("he..o",st)
print(output)
output1=re.findall("he.*o",st)
print(output1)
output2=re.findall("he.{2}o",st)
print(output2)
output3=re.findall("a|e|i|o|u",st)
print(output3)'''

me="i have a 1 apple and 2 orange"
numberofdigit=re.findall("\d",me)
print(numberofdigit)
nonenumberofdigit=re.findall("\D",me)
print(nonenumberofdigit)
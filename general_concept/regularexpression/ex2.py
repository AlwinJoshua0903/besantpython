import re
txt="Python is a high-level, general-purpose programming language. It is design philosophy emphasizes code readability with the use of significant indentation"
print(txt)
numberofwords=re.split(" ",txt)
print(numberofwords)
print(len(numberofwords))
unique=set(numberofwords)
print(unique)
print(len(unique))
output=dict()
for a in numberofwords:
    if a in output:
        output[a]+=1
    else:
        output[a]=1
print(output)
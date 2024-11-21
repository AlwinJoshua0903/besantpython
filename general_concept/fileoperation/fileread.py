import csv
import os.path
fileexists=os.path.isfile('studentout.csv')
print(fileexists)
if fileexists:
    print('file exist')
    with open('studentout.csv','r',newline='')as file:
        reader=csv.reader(file)
        for a in reader:
            print(a)
else:
    print('file does not exist')

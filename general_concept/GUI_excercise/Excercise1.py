from tkinter import *
from tkcalendar import DateEntry
from general_concept.CRUDoperation import insertstudent
root=Tk()
root.title('Python')
root.geometry('400x400')
id=IntVar()
name=StringVar()
mark1=IntVar()
mark2=IntVar()
mark3=IntVar()
Gender=StringVar()
id.set('')
name.set('')
mark1.set('')
mark2.set('')
mark3.set('')
Label(root,text='Student_id').grid(row=0,column=0)
Entry(root,textvariable=id).grid(row=0,column=1)
Label(root,text='Student_name').grid(row=1,column=0)
Entry(root,textvariable=name).grid(row=1,column=1)
Label(root,text='Mark1').grid(row=2,column=0)
Entry(root,textvariable=mark1).grid(row=2,column=1)
Label(root,text='Mark2').grid(row=3,column=0)
Entry(root,textvariable=mark2).grid(row=3,column=1)
Label(root,text='Mark3').grid(row=4,column=0)
Entry(root,textvariable=mark3).grid(row=4,column=1)
Label(root,text='Gender').grid(row=5,column=0)
Radiobutton(root,variable=Gender,text="Male",value=1).grid(row=5,column=1)
Radiobutton(root,variable=Gender,text="Female",value=2).grid(row=5,column=2)
Label(root,text='DOB').grid(row=6,column=0)
datebirth=DateEntry(root)
datebirth.grid(row=6,column=1)

statelist=['Tamilnadu','Andhra pradesh','kerala','goa','delhi']
student_loc=StringVar(root)
student_loc.set('select a state')
OptionMenu(root,student_loc,*statelist).grid(row=7,column=1)
Label(root,text='course_available',bg='lightgreen').grid(row=8,column=0)
sql_value=IntVar()
python_value=IntVar()
Django_value=IntVar()
Flask_value=IntVar()
rest_api=IntVar()
Checkbutton(root,variable=sql_value,text='sql',onvalue=1,offvalue=0).grid(row=8,column=1)
Checkbutton(root,variable=python_value,text='python',onvalue=1,offvalue=0).grid(row=8,column=2)
Checkbutton(root,variable=Django_value,text='Django',onvalue=1,offvalue=0).grid(row=8,column=3)
Checkbutton(root,variable=Flask_value,text='Flask',onvalue=1,offvalue=0).grid(row=8,column=4)
Checkbutton(root,variable=rest_api,text='RestAPI',onvalue=1,offvalue=0).grid(row=8,column=5)

def savetodb():
    idv=id.get()
    namev=name.get()
    mark1v=mark1.get()
    mark2v=mark2.get()
    mark3v=mark3.get()
    if Gender.get()=='1':
        Genderv='Male'
    else:
       Genderv='Female'
    dobv=datebirth.get()
    loc=student_loc.get()
    ci=[]
    if sql_value.get():
        ci.append('Sql')
    if python_value.get()==1:
        ci.append('Python')
    if Django_value.get() == 1:
        ci.append('Django')
    if Flask_value.get() == 1:
        ci.append('Flask')
    if rest_api.get() == 1:
        ci.append('rest_api')
    cifinal='-'.join(ci)

    insertstudent(idv,namev,mark1v,mark2v,mark3v,Genderv,dobv,loc,cifinal)
    root.destroy()
    #print(idv,namev,mark1v,mark2v,mark3v,total,avg,Grv)

Button(root,text='submit',command=savetodb).grid(row=9,column=1)
root.mainloop()
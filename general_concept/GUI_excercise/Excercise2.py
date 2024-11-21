from tkinter import *
from tkinter import messagebox
root=Tk()
root.title('Python')
root.geometry('400x400')
num1=IntVar()
operation=StringVar()
num2=IntVar()
num3v=IntVar()
num1.set('')
operation.set('')
num2.set('')
num3v.set('')
Label(root,text='Number1').grid(row=0,column=0)
Entry(root,textvariable=num1).grid(row=0,column=1)
Label(root,text='Number2').grid(row=1,column=0)
Entry(root,textvariable=num2).grid(row=1,column=1)
Label(root,text='operation').grid(row=2,column=0)
Entry(root,textvariable=operation).grid(row=2,column=1)
def savetodb():
    num1v=num1.get()
    num2v=num2.get()
    operationv=operation.get()
    if operationv=='+':
        num3v.set(num1v+num2v)
    elif operationv=='-':
        num3v.set(num1v-num2v)
    elif operationv == '*':
        num3v.set(num1v * num2v)
    elif operationv == '/':
        num3v.set(num1v / num2v)
    else:
        messagebox.showerror("input is wrong")
Button(root, text='result',bg='blue', command=savetodb).grid(row=3, column=1)
Entry(root,textvariable=num3v).grid(row=4,column=1)
root.mainloop()

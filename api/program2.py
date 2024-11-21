from tkinter import *
import requests
root=Tk()
root.title('Weather Prediction')
root.geometry('600x700' )
Label(root,text="Enter the city").grid(row=0,column=0)
c=StringVar()
Entry(root,textvariable=c).grid(row=0,column=1)
def fetch():
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=3b38f7256941d04dc249f965f535ca29&q='
    city = c.get()
    url = api_address + city
    json_data = requests.get(url).json()
    lo.set(json_data['coord']['lon'])
    la.set(json_data['coord']['lat'])
    de.set(json_data['weather'][0]['description'])

Button(root,text="Submit",command=fetch).grid(row=1,column=1)
lo=StringVar()
Label(root,text="Longitude").grid(row=2,column=0)
Entry(root,textvariable=lo).grid(row=2,column=1)
la=StringVar()
Label(root,text="Latitude").grid(row=3,column=0)
Entry(root,textvariable=la).grid(row=3,column=1)
de=StringVar()
Label(root,text="Description").grid(row=4,column=0)
Entry(root,textvariable=de).grid(row=4,column=1)
root.mainloop()
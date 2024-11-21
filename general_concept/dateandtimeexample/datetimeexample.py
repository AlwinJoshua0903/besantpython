import datetime
import datetime as dt
currenttime=dt.datetime.now()
print(currenttime)
currentday=dt.date.today()
print(currentday)
print(f"currentyear={currenttime.year}")
print(f"currentmonth={currenttime.month}")
print(f"currentday={currenttime.day}")
print(f"currentnanosceond={currenttime.microsecond}")

#create a specific date and time
mycurrentdatetime=dt.datetime(2020,9,20,10,25,9,564590)
print(mycurrentdatetime)
mydate=dt.date(2023,12,9)
print(mydate)
mytime=dt.time(10,12,9,567890)
print(mytime)
orderdate=dt.datetime(2023,9,6,12,45,58,675432)
print(orderdate)
receivedate=dt.datetime(2023,9,25,6,23,34,563212)
print(receivedate)
calcul=receivedate-orderdate
print(calcul)
print(calcul.days)
no_of_days=10
future=currenttime+datetime.timedelta(hours=no_of_days)
print(future)
print(currenttime.weekday())#start with monday =0
print(currenttime.isoweekday())#start with monday=1
if currenttime.weekday()==0:
    print("monday")
elif currenttime.weekday()==1:
    print("tuesday")
elif currenttime.weekday()==2:
    print("wednesday")
elif currenttime.weekday()==3:
    print("thursday")
elif currenttime.weekday()==4:
    print("friday")
elif currenttime.weekday()==5:
    print("saturday")
else:
    print("sunday")
print(currenttime)
print(currenttime.isoformat())
print(currenttime)
updatehour=currenttime.replace(hour=13)
print(updatehour)
updatemonth=currenttime.replace(month=12)
print(updatemonth)
mydate=dt.date(2023,12,9)
print(mydate)
mytime=dt.time(10,12,9,567890)
print(mytime)
combine=dt.datetime.combine(mydate,mytime)
print(combine)
v=1633072800
v1=dt.datetime.fromtimestamp(v)
print(v1)
print(currenttime.strftime('%Y-%m-%d'))
print(currenttime.strftime('%d/%m/%Y'))
print(currenttime.strftime('%B'))
print(currenttime.strftime('%B %d,%Y'))
print(currenttime.strftime('%Y/%m/%d %H:%M'))
print(currenttime.strftime('%Y/%m/%d %H:%M:%S'))
print(currenttime.strftime('%Y/%m/%d %H:%M:%S %p'))


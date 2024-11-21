#series-row index
#Dataframe-row index,column index
# different ways to creating a pandas
#from csv
# manually
#from dataframe

#Series
import pandas as pd
series1=pd.Series([2,3,4,5,6])
print(series1)
print(series1.values)
print(series1.index)
series2=pd.Series([4,8,9,0,2],index=[0,1,2,3,4])
print(series2)
print(series2.values)
print(series2.index)
series2.index=['a','c','d','f','j']
print(series2)
print(series2.values)
print(series2.index)
dict1={'apple':50,'orange':51,'bannana':52,'kiwi':53,'grapes':54}
series3=pd.Series(dict1)
print(series3)

newindex=['apple','orange','grapes','bannana','kiwi']
series4=pd.Series(dict1,index=newindex)
print(series4)
print('apple'in series3)
print('pineapple'in series3)

print(series2)
'''print(series2[3])
print(series2+3)'''

#Dataframe
st=[[1,'abc'],[2,'def'],[3,'ghi']]
print(st)
stdataframe=pd.DataFrame(st)
print(stdataframe)
stdataframe1=pd.DataFrame(st,columns=['s.no','sname'])
print(stdataframe1)
stdataframe2=pd.DataFrame(st,columns=['s.no','sname'],index=['a','b','c'])
print(stdataframe2)

#example

st=[[1,'A',10,20,25],[2,'B',9,17,14],[3,'C',8,23,10],[4,'D',25,25,25],[5,'E',12,17,24]]
print(st)
stdata=pd.DataFrame(st)
print(stdata)
stdata1=pd.DataFrame(st,columns=['s.no','sname','M1','M2','M3'])
print(stdata1)
stdata2=pd.DataFrame(st,columns=['s.no','sname','M1','M2','M3'])
print(stdata2)
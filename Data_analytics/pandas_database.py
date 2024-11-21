import mysql.connector
import pandas as pd
from matplotlib import pyplot as plt

config = {
    'user': 'root',
    'password': 'Alwinbhavi@0903',
    'host': 'localhost',
    'database': 'classicmodels'
}
cnx = mysql.connector.connect(**config)
sqlquery="""select b.*,a.orderdate,a.status,c.*
From
orders a
 inner join 
 orderdetails b 
 on a.orderNumber=b.orderNumber
inner join customers c
on a.customerNumber=c.customerNumber
where a.orderNumber between 10100 and 10110
"""
dataframe=pd.read_sql(sqlquery,cnx)
'''print(dataframe)
print(dataframe.shape)
print(dataframe.dtypes)
print(dataframe.columns)'''
dataframe['Amount']=dataframe['quantityOrdered'] * dataframe['priceEach']
ordernumberwisesale=dataframe.groupby('orderNumber')['Amount'].sum()
print(ordernumberwisesale)
ordernumberwisesale.plot(kind='bar')
plt.show()



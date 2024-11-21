import numpy as np
a=[[12,3,4],[2,5,6],[3,7,8]]
b=np.array(a)
print(a)
print(b)

arr1=np.random.randint(0,10,size=20)
print(arr1)
uni=np.unique(arr1)
print(uni)
uni,count=np.unique(arr1,return_counts=True)
print(uni)
print(count)
#Empty List
L=[]
print(L)

#List

#single list

L1=[98,92,94,84,37]
print(L1)

#indexing

#Positive Index

L1=[98,92,94,84,37]
print(L1[3])

#Negative index

L1=[98,92,94,84,37]
print(L1[-4])

#Nested List

L2=[[11,12,13],[14,15,16],[17,18,19]]
print(L2[2])
print(L2[2][0])

#slicing

L3=[8,4,14,12,3,7]
print(L3[ :4])
print(L3[2:])
print(L3[2:4])
print(L3[2:-1])
print(L3[1:-2])

#step
print(L3[0:4:2])

#In-Build function

print(sum(L3))
print(max(L3))
print(min(L3))
print(len(L3))

#find the available function in List

print(dir(L3))

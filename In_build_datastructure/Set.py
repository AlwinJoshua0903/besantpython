# * means important
#point to remember
#duplicate value not printed
#o/p order will not same as input
#(so that indexing,slicing,will not work)
set={1,2,3,4,5}
print(set)
print(dir(set))
#copy
s5=set.copy()
print(s5)
#clear
s5.clear()
print(s5)
#add
s5.add(7)
s5.add(8)
s5.add(7)
print(s5)
s6={1,2,3,4,5,6}
s7={1,2,4,7,8,9}
s8={1,2,7,8,9,10}
#intersection(common in sets)
interoutput=s6.intersection(s7)
print(interoutput)
interoutput1=s6.intersection(s7,s8)
print(interoutput1)
#intersection Symbol
x=s6&s7
print(x)
y=s6&s7&s8
print(y)
#union(combined the sets but not print duplicate)
unionoutput=s6.union(s7)
print(unionoutput)
unionoutput1=s6.union(s7,s8)
print(unionoutput1)
#union symbol
a=s6|s7
print(a)
b=s6|s7|s8
print(b)
#difference symbol(only return the first set)
diff=s6-s7
print(diff)
diff1=s6-s7-s8
print(diff1)
#difference(remove common element only return the first set element)
dif=s6.difference(s7)
print(dif)
dif1=s6.difference(s7,s8)
print(dif1)
#symetric difference(remove common element return the both set element)
symetric=s6.symmetric_difference(s7)
print(symetric)
symetric1=s6.symmetric_difference(s7)
print(symetric1)
#symetric difference(remove common element return the both set element)
symetrican=s6^s7
print(symetrican)
symetrican1=s6^s7^s8
print(symetrican1)
#pop(cannot identify the which element is removed from the set)
print(s8)
s8.pop()
print(s8)
s9={1,4,7,11,13,8}
# * diff between discard vs remove
#discard and remove both are remove the element from the set
#discard(does not through the error while executed whether the element are in the set or not)
print(s9)
s9.discard(12)
print(s9)
#remove(it must through error whether the element are not in the set)
s9.remove(13)
print(s9)
s10={'a','b','c'}
s11={'a','b'}
#issubset(return true or false whether the element in the set must be element in another set)
print(s10.issubset(s11))
print(s11.issubset(s10))
#superset(viceversa of issubset)
print(s10.issuperset(s11))
print(s11.issuperset(s10))
#isdisjoint
s12={'A','B','C'}
s13={'X','Y','Z'}
print(s12.isdisjoint(s13))
print(s13.isdisjoint(s12))
#update
s14={1,2,3}
s15={7,8}
s14.update(s15)
print(s14)
print(s15)
#difference_update
s7.difference_update(s8)
print(s7)
#intersection_update
s7.intersection_update(s7)
print(s7)
#symmetric_difference_update
s7.symmetric_difference_update(s8)
print(s7)




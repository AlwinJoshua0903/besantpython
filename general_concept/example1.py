L=[1,2,4,9,8,11,12,14,17,19]
print(L)
print(L[3])
print(L[-4])
print(L[:])
print(L[2:])
print(L[:4])
print(L[::2])
print(L[::3])
print(L[3:7])
print(L[7:3:-1])

c2022={'A','B','C','D','E'}
c2023={'A','F','E','Z','H'}
c2024={'E','A','D','Z','F'}
#Identify all the unique customers?
print(c2022.union(c2023,c2024))
#Identify the Customers whose  a order in all years?
print(c2022&c2023&c2024)
#order in 2022 But no in 2023?
print(c2022-c2023)
#order in 2022 But no in 2023 but order in 2024?
print((c2022-c2023)&c2024)

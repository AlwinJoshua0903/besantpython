country_list=['Japan','United States Amercia','India','Srilanka','United Kingdom']
'''for a in range(len(country_list)):
    splitvalue=country_list[a].split(' ')
    if len(splitvalue)==1:
        c=splitvalue[0]
        print(c[0:3])
    else:
        s=""
        for b in range(len(splitvalue)):
            c=splitvalue[b]
            s+=c[0]
        print(s)'''
'''initialmax=len(country_list[0])
for c in country_list:
    print(initialmax,c,len(c))
    if initialmax<len(c):
        initialmax=len(c)
        maxword=c
        print(maxword)'''

L = [123, 457, 912, 1437, 2314, 811, 456,656]

# Calculate the sum of digits for each number in the list
#List comprehension with an embedded generator expression
sum_of_digits_list = [sum(int(digit) for digit in str(number)) for number in L]

# Find the maximum of these digit sums
max_digit_sum = max(sum_of_digits_list)



print("The maximum sum of digits is:", max_digit_sum)

L = [123, 457, 912, 1437, 2314, 811, 456, 656,7898]

# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Find the number in L with the maximum sum of digits
max_digit_sum_number = max(L, key=sum_of_digits)
max_digit_sum = sum_of_digits(max_digit_sum_number)

print("The number with the maximum sum of digits is:", max_digit_sum_number)
print("The maximum sum of digits is:", max_digit_sum)











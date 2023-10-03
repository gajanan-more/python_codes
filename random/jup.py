# l1 = [1,2,3,4,5,6,77,8,9,9,90,34,45,45,2,546,436,536]
#
# sum_odd = 0
#
# sum_even = 0
#
# even_count = 0
#
# for i in l1:
#     if i % 2 == 0:
#         sum_even += i
#         even_count  += 1
#     else:
#         sum_odd += i
#
#
# print("Odd Numbers: ",len(l1) - even_count, " and it's sum is: ",sum_odd)
#
# print("Even Numbers: ",even_count, " and it's sum is: ",sum_even)

"""
F2C = F * 16^2 + 2 * 16^1 + C * 16 ^ 0
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F
"""

mydict = {'A': 10, 'B': 11, 'C':12, 'D':13, 'E': 14, 'F': 15}

s = "F2C"
output = 0
j = 0

for i in s[::-1]:
    if i in mydict:
        x = int(mydict[i])
    else:
        x = int(i)
    output = output + (x * 16 ** j)
    j += 1

#x = int(i) if i in mydict int(mydict[i])

print(output)


#def hex_dec(num):


"""
Given multiple numbers and a number n, the task is to print the remainder after multiplying all the numbers divided by n.
Examples:

Input : arr[] = {100, 10, 5, 25, 35, 14}, n = 11
Output : 9
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = int(input("Enter your number: "))

sum = 1

for x in l1:
    sum *= x

print(sum % n)
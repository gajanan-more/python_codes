"""
*
* *
* * *
* * * *
* * * * *
"""

n = int(input("Enter how many rows you want: "))
num = 1

for i in range(1,n+1):
    for j in range(1, i+1):
        if num < 10:
            print("0" + str(num), end=" ")
        else:
            print(num, end=" ")
        num += 1
    print("\r")
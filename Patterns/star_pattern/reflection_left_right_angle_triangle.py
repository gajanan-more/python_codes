"""
* * * * *
* * * *
* * *
* *
*
"""

n = int(input("Enter how many rows you want: "))

for i in range(n,0,-1):
    for j in range(1, i+1):
        print("*", end=" ")
    print("\r")
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

    print("  " * (n - i), end="") # Double space * (n - i)

    for j in range(i):
        print(num, end=" ")
        num += 1

    print()

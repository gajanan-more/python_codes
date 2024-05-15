"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
n = int(input("Enter how many rows you want: "))

for i in range(n,0,-1):

    print("  " * (n - i), end="") # Double space * (n - i)

    for j in range(i):
        print("*", end=" ")

    print()

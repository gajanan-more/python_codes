"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
n = int(input("Enter how many rows you want: "))
num = 1

for i in range(n,0,-1):

    print("  " * (n - i), end="") # Double space * (n - i)

    for j in range(i):
        if num < 10:
            print("0" + str(num), end=" ")
        else:
            print(num, end=" ")
        num += 1

    print()

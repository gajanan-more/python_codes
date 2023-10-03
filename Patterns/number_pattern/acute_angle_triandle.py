"""
       1
      2 3
    4  5 6
  7  8  9  10
11 12 13 14 15
"""
n = int(input("Enter how many rows you want: "))
num = 1

for i in range(1,n+1):

    print(" " * (n - i), end="")

    for j in range(i):
        if num < 10:
            print("0" + str(num), end=" ")
        else:
            print(num, end=" ")
        num += 1

    print()
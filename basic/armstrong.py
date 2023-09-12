n1 = int(input("Enter your number"))

num = n1

l1 = list()

while num != 0:
    l1.append(num % 10)
    num //= 10

for x in range(len(l1)):
    num = num + l1[x] ** len(l1)

if n1 == num:
    print("Number is armstrong")
else:
    print("Number is not armstrong")




l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_ele = 2

l2 = []
x = reverse_ele

for x in range(reverse_ele, len(l1)):
    l2.append(l1[x])

for y in range(reverse_ele):
    l2.append(l1[y])

l1 = l2

#l3 = l1[reverse_ele:] + l1[:reverse_ele]

print(l1)
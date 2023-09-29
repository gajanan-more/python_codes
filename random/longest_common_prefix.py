"""
list_comprehensions of words
find longest common prefix

l = [start, started, startup, stop]
"""

l = ["start", "started", "startup", "starting","startedd"]

out_prefix = ""

count = 0
l.sort()

for i in l[0]:
    for j in l:
        if i in j:
            count += 1

    if count == len(l):
        out_prefix += i
        count = 0
    else:
        break

print(out_prefix)







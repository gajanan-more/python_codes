s = "ABCD"
l = []
out = ""
expect = "CBAD"

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        out = out + s[j]

    out = out + s[:i + 1]
    l.append(out)
    out = ""

if expect in l:
    print('YES')
else:
    print('NO')

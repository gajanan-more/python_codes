# str = "A/B$C"
#
# # str = "C/B$A"
# # 65 to 90
# n = len(str) - 1
# out_str = []
#
# for i in range(len(str) - 1):
#     out_str.append("0")
#
# strt = 0
#
# while True:
#     if str[n].isalpha():
#         out_str[strt] = str[n]
#         strt += 1
#     else:
#         a = str[n]
#         out_str[n] = a
#         strt += 1
#
#     n -= 1
#
#     if n == 0:
#         out_str.append(str[n])
#
#     if n == 0:
#         break
#
# output = ""
#
# print(out_str)
#
#
# for i in out_str:
#     output += i
#
# print(output)
#
# """
# 1. All alpha
# 2. All special chars
# 3. Begin with alpha
# 4. Begin with spl
# 5. Begin and end with alpha
# 6. Begin and end with spl
# 7. Single char string
# 8. Empty String
# """


"""
"Finding the  Kth last non-repetitive character in a string
K - 2
Input - asciikgg
Output - c"
"""



#
# str = "asciikgg"
#
# k = 3
# count = 0
# my_dict = {}
#
# if str == "":
#     print("String is empty")
#
# elif len(str) == 1:
#     print(str)
#
# else:
#
#     for i in str:
#         if i in my_dict:
#             my_dict[i] += 1
#         else:
#             my_dict[i] = 1
#
#     l = []
#
#     for i in my_dict:
#         if my_dict[i] == 1:
#             l.append(i)
#
#     if l is None:
#         print("No repetative char")
#
#     else:
#         for i in l[::-1]:
#             k -= 1
#             if k == 0:
#                 print(i)





"""
Check if two strings are circular.
A string pair is circular if its rotated version of the original string.

Input_1 - "ABCD" and "CDAB"
Output_1 - True

Input_2 - "XYCB" and "BCXY"
Output_2 - False
"""
strg = "ABCD"

check_strg = "CDAB"

n = len(strg) - 1
l = []
output = ""
for i in range(n):
    for j in range(i+1, i+4):
        if (j > len(strg) - 1):
            output = output + strg[0:i]
            break
        else:
            output = output + strg[j]



    l.append(output)


print(l)
















































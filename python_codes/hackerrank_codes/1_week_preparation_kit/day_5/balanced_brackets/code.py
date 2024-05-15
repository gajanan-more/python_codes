#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    open_brc = ["{", "(", "["]
    close_brc = ["}", ")", "]"]
    l = []

    for i in s:
        if i in open_brc:
            l.append(i)

        elif i in close_brc:
            if l == []:
                return "NO"
            elif i == "}" and l[-1] != "{":
                return "NO"
            elif i == ")" and l[-1] != "(":
                return "NO"
            elif i == "]" and l[-1] != "[":
                return "NO"
            else:
                l.pop()

    if l == []:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

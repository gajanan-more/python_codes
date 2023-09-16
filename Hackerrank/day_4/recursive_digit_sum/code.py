#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    def helper(n):
        sum = 0
        for i in n:
            sum += int(i)

        sum = str(sum)

        if len(sum) == 1:
            return sum
        else:
            return helper(sum)

    # p = n * k
    p = str(helper(n) * k)

    return helper(p)

    # strg = n

    # for i in range(1,k):
    #     n += strg

    # num = int(n)

    # if num % 10 == num:
    #     return num

    # sum = 0

    # while True:
    #     sum = sum + (num % 10)

    #     num = num // 10

    #     if sum < 10 and num == 0:
    #         return sum
    #     elif num == 0:
    #         num = sum
    #         sum = 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

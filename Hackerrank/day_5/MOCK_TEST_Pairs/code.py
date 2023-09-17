#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    # Write your code here

    total = 0

    # Solution 1 (Not optimum: 13/18 Pass)
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if arr[i] - arr[j] == k:
    #             total += 1

    # Solution 2 (18/18)

    my_dict = {}

    for i in arr:
        my_dict[i] = 1
        if i + k in my_dict:
            total += 1
        if i - k in my_dict:
            total += 1

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

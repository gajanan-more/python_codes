#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min = 0
    max = 0

    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            if j != i:
                sum += arr[j]

        if min == 0 and max == 0:
            min = sum
            max = sum
        else:
            if sum < min:
                min = sum
            elif sum > max:
                max = sum

    print(min, max)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

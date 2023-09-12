#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    arr_len = len(arr)
    result = []
    my_dict = {}

    for i in range(0, 100):
        result.append(0)

    for i in arr:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    for i in my_dict:
        result[i] = my_dict[i]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

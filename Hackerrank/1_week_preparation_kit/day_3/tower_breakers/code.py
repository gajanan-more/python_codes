#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


"""
Both players always play optimally that means whenever they get a chance, they will always reduce the height of tower to 1
"""
def towerBreakers(n, m):
    # Write your code here
    # If number of tower is 1, Player 1 will always win.
    if n == 1:
        return 1
    # If Height of tower is 1, Player 2 will always win
    elif m == 1:
        return 2
    else:
        # If the number of tower is even, Player 2 will always win
        if n % 2 == 0:
            return 2
        # If the number of tower is odd, Player 1 will always win
        else:
            return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

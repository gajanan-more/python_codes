#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    l = []
    s = ""

    """
    Converting the each item from grid to list and then sorted each item and replaced 
    existing item with sorted item 
    """
    for i in range(len(grid)):
        for j in grid[i]:
            l.append(j)

        l.sort()

        for m in l:
            s += m

        grid[i] = s

        l.clear()
        s = ""

    count = 0

    """
    Checking if columns are also in alphabetical order
    """

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if j == len(grid) - 1:
                break
            else:
                if ord(grid[j][i]) > ord(grid[j + 1][i]):
                    count += 1

        if count > 0:
            return "NO"

    if count == 0:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

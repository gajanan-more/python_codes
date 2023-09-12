#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    list1 = []
    result = ""

    for i in s:
        if i == 'A' or i == 'M' or i == 'P':
            pass
        else:
            list1.append(i)

    if "AM" in s:

        if list1[0:2] == ['1', '2']:
            result = "00"

            for j in range(2, len(list1)):
                result += list1[j]

        else:
            for j in range(len(list1)):
                result += list1[j]

    elif "PM" in s:
        if list1[0:2] == ['1', '2']:
            for j in range(len(list1)):
                result += list1[j]

        elif list1[0] == '0':
            time = 12 + int(list1[1])
            result = str(time)
            for j in range(2, len(list1)):
                result += list1[j]

        elif list1[1] == '1':
            time = 12 + 11
            result = str(time)
            for j in range(2, len(list1)):
                result += list1[j]

        else:
            time = 12 + 10
            result = str(time)
            for j in range(2, len(list1)):
                result += list1[j]

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

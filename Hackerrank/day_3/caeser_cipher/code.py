#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

"""
ASCII code for the character A is 65, and 90 is for Z. 
Similarly, ASCII code 97 is for a, and 122 is for z.
You can get the ASCII value of a character by using the ord() function
chr() function is used to get a string representing of a character which points to ASCII value
"""


def caesarCipher(s, k):
    # Write your code here
    result = ""

    for i in s:
        if i == " ":
            result += i
        elif (i.isupper()):
            result += chr((ord(i) + k - 65) % 26 + 65)
        # check if a character is lowercase then encrypt it accordingly
        elif (i.islower()):
            result += chr((ord(i) + k - 97) % 26 + 97)
        else:
            result += i

    return result

    # for i in s:
    # if ord(i) >= 97 and ord(i) <= 122:
    #     val = ord(i) + k

    #     while True:
    #         if val > 122:
    #             val = ord('a') + (val - 123)
    #         else:
    #              result += chr(val)
    #              break

    # elif ord(i) >= 65 and ord(i) <= 90:
    #     val = ord(i) + k

    #     while True:
    #         if val > 122:
    #             val = ord('a') + (val - 91)
    #         else:
    #              result += chr(val)
    #              break
    # else:
    #     result += i




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

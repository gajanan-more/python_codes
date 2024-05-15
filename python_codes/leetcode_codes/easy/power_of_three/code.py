import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Appraoch 1
        if n <= 0:
            return False

        while n % 3 == 0:
            n /= 3

        return n == 1

        # Appraoch 2
        # if n <= 0:
        #     return False
        # elif n == 1 or n == 3:
        #     return True
        # elif n % 3 == 0:
        #     e = log(n,3)
        #     x = round(e,1)
        #     if pow(3,x) == n:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False

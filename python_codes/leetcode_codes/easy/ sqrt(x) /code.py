class Solution:
    def mySqrt(self, x: int) -> int:
        # n = 1

        # while n * n <= x:
        #     n += 1

        first = 1
        last = x

        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            while first <= last:
                mid = (first + last) // 2

                if mid * mid == x:
                    return mid
                elif mid * mid > x:
                    last = mid - 1
                elif mid * mid < x:
                    first = mid + 1

        return last
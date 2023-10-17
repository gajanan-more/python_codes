# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Iterative

        # for i in range(n+1):
        #     if isBadVersion(i):
        #         return i
        #         break

        # Binary Search

        start = 1
        end = n

        while start < end:
            mid = (start + end) // 2

            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start



class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return n
        f0 = 1
        f1 = 1
        f2 = 0
        for i in range(2, n + 1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2

        return f2
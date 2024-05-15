class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sum = 0
        y=x
        if x < 0:
            return False
        else:
            while True:
                rem = x%10
                sum = sum*10 + rem
                x //= 10
                if x == 0:
                    break
        if sum == y:
            return True
        else:
            return False
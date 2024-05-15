class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alist = []

        if len(s) == 1:
            return False
        else:
            for l in range(len(s)):
                if s[l] == '(' or s[l] == '{' or s[l] == '[':
                    alist.append(s[l])
                else:
                    if not alist:
                        return False
                    elif alist[-1] == '(' and s[l] == ')':
                        alist.pop()

                    elif alist[-1] == '{' and s[l] == '}':
                        alist.pop()

                    elif alist[-1] == '[' and s[l] == ']':
                        alist.pop()

                    else:
                        alist.append(s[l])

        if alist:
            return False
        else:
            return True
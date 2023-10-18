class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = []
        if len(s) == 1:
            return s
        else:
            # Time Issue: 132/142 TC Passed
            # """
            #         for i in range(len(s)):
            #             for j in range(i, len(s)+1):
            #                 if i == j:
            #                     pass
            #                 else:
            #                     result.append(s[i:j])

            #         palindrome = ""
            #         for i in result:
            #             if i == i[::-1]:
            #                 if len(i) > len(palindrome):
            #                     palindrome = i

            #     return palindrome
            # """
            def checks(left, right):
                while (left >= 0 and right < len(s) and s[left] == s[right]):
                    left -= 1
                    right += 1

                return s[left + 1:right]

            palindrome = ""

            for i in range(len(s)):
                pal1 = checks(i, i)
                if len(pal1) > len(palindrome):
                    palindrome = pal1

                pal2 = checks(i, i + 1)
                if len(pal2) > len(palindrome):
                    palindrome = pal2

            return palindrome

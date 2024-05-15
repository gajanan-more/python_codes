class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            len_n = len(needle)

            for i in range(len(haystack)):
                if haystack[i:i+len_n] == needle:
                    return i
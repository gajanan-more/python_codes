class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        s = strs[0]

        for i in range(1, len(strs)):
            string = strs[i]
            curr = ""
            index = 0

            while index < len(s) and index < len(string):
                if s[index] == string[index]:
                    curr += string[index]
                    index += 1
                else:
                    break

            s = curr
        return s




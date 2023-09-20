class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        l = s.split(" ")

        z = ""

        for i in l[::-1]:
            if i.isalpha():
                z = i
                break

        return len(z)
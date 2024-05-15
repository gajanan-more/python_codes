class Solution:
    def isPalindrome(self, s: str) -> bool:

        output = ""

        s = s.lower()

        if len(s) == 1:
            return True
        else:
            if " " in s:
                for i in s.split(" "):
                    for j in range(len(i)):
                        if i[j].isalnum():
                            output += i[j]

            elif " " not in s:
                for i in s:
                    if i.isalnum():
                        output += i

            if output == output[::-1]:
                return True
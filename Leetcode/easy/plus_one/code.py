class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strg = ""

        if len(digits) == 1:
            a = str(int(digits[0]) + 1)

            if len(a) == 1:
                digits[0] = int(a)
                return digits
            else:
                digits.clear()
                for i in a:
                    digits.append(int(i))

                return digits

        for i in digits:
            strg += str(i)

        strg = str(int(strg) + 1)

        digits.clear()
        for i in strg:
            digits.append(int(i))

        return digits

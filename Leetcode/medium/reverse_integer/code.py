class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)

        output = ""

        if x < 0:
            for i in y[:0:-1]:
                output += i

            x = 0 - int(output)
        else:
            for i in y[::-1]:
                output += i

            x = int(output)

        if x > (2 ** 31) - 1 or x < (-2 ** 31):
            return 0
        else:
            return x



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """

        """

        if len(s) == 1 or numRows >= len(s) or numRows == 1:
            return s

        rows = [[] for row in range(numRows)]

        index = 0
        step = 1

        output = ""

        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in rows:
            for j in i:
                output += j

        return output



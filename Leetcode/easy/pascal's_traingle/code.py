class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        triangle = []
        row = []

        for i in range(numRows):
            if i == 0:
                row = [1]
            else:
                prev_row = triangle[-1]

                for j in range(0, i + 1):
                    if j == 0:
                        row.append(prev_row[0])
                    elif j == i:
                        row.append(prev_row[-1])
                    else:
                        row.append(prev_row[j - 1] + prev_row[j])

            triangle.append(row)
            row = []

        return triangle
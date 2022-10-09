from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # First row
        result = [[1]]
        if numRows > 1:
            # Seconde row 
            result.append([1,1])

        for i in range(2,numRows):
            row = [1]
            for j in range(i-1) :
                row.append(result[i -1][j] + result[i -1][j + 1])
            # append last element
            row.append(1)
            result.append(row)

        return result

solution = Solution()
print(solution.generate(10))
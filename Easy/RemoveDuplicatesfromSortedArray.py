from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = set(nums)
        return list(x),len(x)
solution = Solution()
print(solution.removeDuplicates([1,1,1,1]))
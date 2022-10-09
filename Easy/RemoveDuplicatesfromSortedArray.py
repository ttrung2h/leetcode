from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for num in nums:
            x = len(nums)
            a = nums.count(num)
            if nums.count(num) > 1:
                for i in range(a - 1):
                    nums.remove(num)

        if nums.count(nums[len(nums) - 1]) > 1:
            nums.remove(nums[len(nums) - 1])
        
        return nums,len(nums)

solution = Solution()
print(solution.removeDuplicates([1,1,1,1]))
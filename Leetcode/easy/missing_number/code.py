class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Approach 1
        nums.sort()

        for i in range(0, len(nums)):
            if i not in nums:
                return i
                break

        return i + 1

        # Approach 2

        # return sum(range(0,len(nums) + 1)) - sum(nums)

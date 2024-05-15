from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        #Approach 1
        # for i in Counter(nums):
        #     if Counter(nums)[i] > (len(nums) / 2):
        #         return i

        #Approach 2
        nums.sort()
        n = len(nums)

        print(nums)

        print(nums[n//2])

        return nums[n//2]
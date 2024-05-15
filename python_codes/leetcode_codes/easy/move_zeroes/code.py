class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if 0 in nums:
        #     nums.sort(reverse=True)

        #     y = nums[0:nums.index(0)]

        #     y.sort()

        #     nums[0:nums.index(0)] = y
        # else:
        #     nums.sort(reverse=True)

        index = 0

        for i in nums:
            if i != 0:
                nums[index] = i
                index += 1

        print(nums)

        while index < len(nums):
            nums[index] = 0
            index += 1

        print(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary Search
        strt = 0
        last = len(nums) - 1

        while strt <= last:
            mid = (last + strt) // 2

            if nums[mid] < target:
                strt = mid + 1
            elif nums[mid] > target:
                last = mid - 1
            else:
                return mid

        return strt

        # if target in nums:
        #     a = nums.index(target)
        #     return int(a)
        # else:
        #     mid = (len(nums)) // 2

        #     if nums[mid] > target:
        #         strt = 0
        #         last = mid
        #     else:
        #         strt = mid
        #         last = len(nums)

        #     for i in range(strt,last,1):
        #         if nums[i] > target:
        #             return i
        #             break

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(m, m + n):
            nums1[i] = nums2[i - m]

        nums1.sort()

        """
        Second Way....Bit longer
        """
        # x = m + n

        # count = []
        # i = 0

        # if nums1 == None or nums2 == None or m == 0 or n == 0:

        #     if nums1 == None:
        #         for i in range(x):
        #             count.append(nums2[i])

        #     if nums2 == None:
        #         for i in range(x):
        #             count.append(nums1[i])

        #     if m == 0:
        #         for i in range(x):
        #             count.append(nums2[i])

        #     if n == 0:
        #         for i in range(x):
        #             count.append(nums1[i])

        # else:

        #     while nums1 or nums2:
        #         if nums1[i] < nums2[i]:
        #             count.append(nums1[i])
        #             nums1.pop(i)
        #             m -= 1
        #         elif nums1[i] > nums2[i]:
        #             count.append(nums2[i])
        #             nums2.pop(i)
        #             n -= 1
        #         elif nums1[i] == nums2[i]:
        #             count.append(nums1[i])
        #             count.append(nums2[i])
        #             nums1.pop(i)
        #             nums2.pop(i)
        #             m -= 1
        #             n -= 1

        #         if m == 0 or n == 0:
        #             break

        #     if m > 0:
        #         for i in range(m):
        #             count.append(nums1[i])

        #     if n > 0:
        #         for i in range(n):
        #             count.append(nums2[i])

        # nums1.clear()

        # for i in range(x):
        #     nums1.append(count[i])

        # return nums1
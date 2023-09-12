"""
Given an array A containing n integers. The task is to check whether the array is Monotonic or not.
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j].
"""

l1 = [2,3,47,6]

l2,l3 = [], []

l2.extend(l1)

l3.extend(l1)

l2.sort()

l3.sort(reverse=True)

if(l1 == l2 or l1 == l3):
    print("Array is monotonic")
else:
    print("Array is not monotonic")
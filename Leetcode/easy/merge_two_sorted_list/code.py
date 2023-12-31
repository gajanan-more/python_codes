# Definition for singly-linked list_comprehensions.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()

        current = node

        while list1 and list2:
            # if list1 == None:
            #     current.next = list2

            # if list2 == None:
            #     current.next = list1

            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        if list1:
            current.next = list1

        if list2:
            current.next = list2

        return node.next

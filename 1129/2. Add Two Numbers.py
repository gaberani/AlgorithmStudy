# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 문제 조건
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Linked List 구현


answer = Solution()
print(answer.addTwoNumbers([2,4,3], [5,6,4]))
# [7, 0, 8]
print(answer.addTwoNumbers([0], [0]))
# [0]
print(answer.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
# [8,9,9,9,0,0,0,1]
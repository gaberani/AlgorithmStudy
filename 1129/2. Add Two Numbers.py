# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
        sum_value = 0
        answer = []
        for i in range(max(len(l1), len(l2))):
            if len(l1) > i:
                sum_value += l1[i]
            if len(l2) > i:
                sum_value += l2[i]
            answer.append(sum_value%10)
            sum_value //= 10
            sum_value = 1 if sum_value else 0
        if sum_value: answer.append(1)

        return answer
        # for i in range(max(len(l1), len(l2))- min(len(l1), len(l2))):





    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1과 l2가 ListNode로 구현되어있음.
        root = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry%10)
            cur = cur.next
            carry //= 10
        return root.next


test = Solution()
print(test.addTwoNumbers([2,4,3], [5,6,4]))
# [7, 0, 8]
print(test.addTwoNumbers([0], [0]))
# [0]
print(test.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9]))
# [8,9,9,9,0,0,0,1]
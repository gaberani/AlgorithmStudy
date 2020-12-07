# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
class Solution(object):
    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        answer = [root.val]
        while root.right == None:

        if not answer:
            answer.append(r.val)
        else:
            answer.append(r.right)

    def rightSideView(self, root):
        # 비어있을 경우
        if root == None:
            return []
        # 초기값
        ans = [root.val]
        # DFS로 반복해서 left, right 각각 붙여내기
        left = ans + self.rightSideView(root.left)
        right = ans + self.rightSideView(root.right)
        if len(right) >= len(left):
            return right
        return right + left[len(right):]

# Example
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# [1, 2, 3, 4]
# TreeNode{val: 1,
#          left: TreeNode{val: 2, left: TreeNode{val: 4, left: None, right: None}, right: None},
#          right: TreeNode{val: 3, left: None, right: None}}
# You have 4 cards each containing a number from 1 to 9.
# You need to judge whether they could operated through *, /, +, -, (, )
# to get the value of 24.

# The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # def operator(a, b, cnt):
        #     if cnt == 0: return a+b
        #     elif cnt == 1: return a-b
        #     elif cnt == 2: return a*b
        #     elif cnt == 3: return a/b

        def dfs(idx, nums_cnt):
            if idx == 4:
                sum_num = 0
            else:
                for i in range(4):
                    visit[i] = 1
                    dfs(idx+1)
                    visit[i] = 0
        visit = [0]*4
        dfs(0)



# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24

# Input: [1, 2, 1, 2]
# Output: False

import math
print(math.ceil(4/(1-2/3)))
print(math.ceil(12))
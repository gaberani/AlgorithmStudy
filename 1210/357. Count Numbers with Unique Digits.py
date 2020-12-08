# Given a non-negative integer n, 
# count all numbers with unique digits, x, where 0 ≤ x < 10^n.

# 0 <= n <= 8
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        # n과 같은 길이를 갖고 있고 
        # set를 써서 중복없애면 길이가 1인 경우 전부 제외
        
# Input: 2
# Output: 91 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
#              excluding 11,22,33,44,55,66,77,88,99
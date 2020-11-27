class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # nums such that a + b + c + d = target?
        # Find all unique quadruplets


answer = Solution()
print(answer.fourSum([1,0,-1,0,-2,2], 0))
print(answer.fourSum([], 0))
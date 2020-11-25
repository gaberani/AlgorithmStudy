class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

answer = Solution()
print(answer.threeSum([-1,0,1,2,-1,-4]))
# Output: [[-1,-1,2],[-1,0,1]]
print(answer.threeSum([]))
# Output: []
print(answer.threeSum([0]))
# Output: []
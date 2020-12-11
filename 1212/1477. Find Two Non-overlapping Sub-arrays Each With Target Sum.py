# two non-overlapping sub-arrays
# you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

# Return the minimum sum of the lengths of the two required sub-arrays,
# or return -1 if you cannot find such two sub-arrays.
class Solution(object):
    # Given an array of integers arr and an integer target.
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        #

test = Solution()
print(test.minSumOfLengths([3, 2, 2, 4, 3])) # 3
print(test.minSumOfLengths([7, 3, 4, 7])) # 7
print(test.minSumOfLengths([4, 3, 2, 6, 2, 3, 4])) # 6
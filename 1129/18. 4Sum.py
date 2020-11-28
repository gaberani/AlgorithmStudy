class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # nums such that a + b + c + d = target?
        # Find all unique quadruplets
        answer = []
        for i in range(L - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            s, e = i + 1, L - 1
            while s < e:
                three = nums[i] + nums[s] + nums[e]
                if three == 0:
                    answer.append((nums[i], nums[s], nums[e]))
                    while s < e and nums[s] == nums[s + 1]: s += 1
                    while s < e and nums[e] == nums[e - 1]: e -= 1
                    s += 1;
                    e -= 1
                elif three < 0:
                    s += 1
                elif three > 0:
                    e -= 1


answer = Solution()
print(answer.fourSum([1,0,-1,0,-2,2], 0))
print(answer.fourSum([], 0))
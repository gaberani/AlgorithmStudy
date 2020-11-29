class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # nums such that a + b + c + d = target?
        # Find all unique quadruplets
        def anySum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return

            if N == 2:
                s, e = 0, len(nums)-1
                while s < e:
                    sum_result = nums[s] + nums[e]
                    if sum_result == target:
                        results.append((result + [nums[s], nums[e]]))
                        s += 1
                        while s < e and nums[s] == nums[s-1]:
                            s += 1
                    elif sum_result < target:
                        s += 1
                    elif sum_result > target:
                        e -= 1
            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        anySum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        anySum(sorted(nums), target, 4, [], results)
        return results


answer = Solution()
print(answer.fourSum([1,0,-1,0,-2,2], 0))
print(answer.fourSum([], 0))
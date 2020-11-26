class Solution(object):
    def threeSum(self, nums):
        # Find all unique triplets
        L = len(nums)
        if L < 3:
            return []

        answer = []
        for i in range(L-2):
            s, e = i+1, L-1
            while s < e:
                three = nums[i] + nums[s] + nums[e]
                if three == 0:
                    answer.append((nums[i], nums[s], nums[e]))
                elif three > 0:
                    s += 1
                elif three < 0:
                    e -= 1

    def SortedthreeSum(self, nums):
        # Find all unique triplets
        L = len(nums)
        if L < 3:
            return []

        nums.sort()
        answer = []
        for i in range(L-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            s, e = i+1, L-1
            while s < e:
                three = nums[i] + nums[s] + nums[e]
                if three == 0:
                    answer.append((nums[i], nums[s], nums[e]))
                    while s < e and nums[s] == nums[s+1]: s += 1
                    while s < e and nums[e] == nums[e-1]: e -= 1
                    s += 1; e -= 1
                elif three < 0:
                    s += 1
                elif three > 0:
                    e -= 1
        return answer

answer = Solution()
# print(answer.threeSum([-1,0,1,2,-1,-4]))
# Output: [[-1,-1,2],[-1,0,1]]
# print(answer.threeSum([]))
# Output: []
# print(answer.threeSum([0]))
# Output: []
print(answer.SortedthreeSum([0, 0, 0]))
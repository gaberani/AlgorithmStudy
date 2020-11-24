# Input: nums = [1,2,3,4]
# Output: false

# Input: nums = [3,1,4,2]
# Output: true

# Input: nums = [-1,3,2,0]
# Output: true

class Solution(object):
    def find132pattern(self, nums):
        L = len(nums)
        for i in range(L-2):
            # nums[i] < nums[k]
            print(nums[i], nums[L-i-1])
            if nums[i] < nums[L-i-1]:
                for j in range(i+1, L-i-1):
                    print(nums[i], nums[L-i-1], nums[j])
                    if nums[L-i-1] < nums[j]:
                        return True
                    else:
                        break
        return False

    def find132pattern2(self, nums):
        from itertools import accumulate
        min_list = list(accumulate(nums, min))
        stack, n = [], len(nums)

        for j in range(n - 1, -1, -1):
            if nums[j] > min_list[j]:
                while stack and stack[-1] <= min_list[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False

answer = Solution()
print(answer.find132pattern([3,1,4,2]))
# print(answer.find132pattern([3,5,0,3,4]))
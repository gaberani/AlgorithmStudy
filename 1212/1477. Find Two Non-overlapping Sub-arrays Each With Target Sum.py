# 슬라이딩 윈도우 알고리즘

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
        L = len(arr)
        if L == 1:
            return -1

        subarrays = []
        sub = []
        for i in range(L):
            sum_result = sum(sub) + arr[i]
            if sum_result == target:
                subarrays += ([sub+[arr[i]]])
                sub = []
            elif sum_result > target:
                if arr[i] == target:
                    sub = []
                    subarrays.append([arr[i]])
                else:
                    sub = [arr[i]]
            elif sum_result < target:
                sub.append(arr[i])
            # print(sub, arr[i], subarrays)
        if sum(sub) == target:
            subarrays.append(sub)
        print(subarrays)

        if len(subarrays) < 2:
            return -1
        subarrays = sorted(subarrays, key= lambda x: len(x))
        return len(subarrays[0])+len(subarrays[1])

    # 슬라이딩 윈도우
    def minSum21(self, arr, target):
        my_Inf = len(arr) + 1
        best_at_i = [my_Inf] * len(
            arr)  # the ith index represents the smallest length subarray we've found ending <= i that sums to target
        best = my_Inf  # output 
        curr_sum = 0  # current sum between left and right
        left = 0
        for right in range(len(arr)):
            # update the running sum
            curr_sum += arr[right]

            # arr is strictly positive, so shrink window until we're not above target
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                # we have a new shortest candidate to consider
                best = min(best, best_at_i[left - 1] + right - left + 1)
                best_at_i[right] = min(best_at_i[right - 1], right - left + 1)
            else:
                # best we've seen is the previous best (overlaps to end if right == 0)
                best_at_i[right] = best_at_i[right - 1]

        if best == my_Inf:
            return -1
        return best

    # 리스트 한 개, 한 번만 for문 돌려서 해결
    def minSum2(self, arr, target):
        i, window, result = 0, 0, float('inf')
        dp = [float('inf')] * len(arr)
        for j, num in enumerate(arr):
            window += num
            while window > target:
                window -= arr[i]
                i += 1
            if window == target:
                now = j - i + 1
                result = min(result, now + dp[i-1])
                dp[j] = min(now, dp[j-1])
            else:
                dp[j] = dp[j - 1]
        return result if result < float('inf') else -1

test = Solution()
print(test.minSumOfLengths([3, 2, 2, 4, 3], 3)) # 2
print(test.minSumOfLengths([7, 3, 4, 7], 7)) # 2
print(test.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6)) # -1
print(test.minSumOfLengths([1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8], 5)) # -1
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

test = Solution()
print(test.minSumOfLengths([3, 2, 2, 4, 3], 3)) # 2
print(test.minSumOfLengths([7, 3, 4, 7], 7)) # 2
print(test.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6)) # -1
print(test.minSumOfLengths([1, 2, 2, 3, 2, 6, 7, 2, 1, 4, 8], 5)) # -1
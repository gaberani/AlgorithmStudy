# Given a triangle, find the minimum path sum from top to bottom.
# Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 1

class Solution(object):
    def minimumTotal(self, triangle):
        global answer
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 각 스텝마다 최소를 더한 path를 구하기
        # dfs
        # 백트래킹없이 완전 탐색

        def dfs(step, cnt, preIdx):
            global answer
            if step == L:
                answer = min(answer, cnt)
            else:
                for i in range(preIdx, preIdx+2):
                    if 0 <= i < step+1:
                        dfs(step+1, cnt+triangle[step][i], i)

        L = len(triangle)
        answer = 2**31
        dfs(0, 0, 0)
        return answer

    def minimumTotal2(self, triangle):
        global answer
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 각 스텝마다 최소를 더한 path를 구하기
        # dfs
        # 백트래킹없이 완전 탐색

        def dfs(step, numList):
            global answer
            if step == L:
                print(numList)
                for numInfo in numList:
                    answer = min(answer, numInfo[0])
            else:
                tmp = []
                for numInfo in numList:
                    num, preIdx = numInfo
                    for i in range(preIdx, preIdx+2):
                        if 0 <= i < step+1:
                            tmp.append([num+triangle[step][i], i])
                dfs(step+1, tmp)

        L = len(triangle)
        answer = 2**31
        dfs(1, [[triangle[0][0], 0]])
        return answer

test = Solution()
print(test.minimumTotal2([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(test.minimumTotal2([[-1],[3,2],[-3,1,-1]]))
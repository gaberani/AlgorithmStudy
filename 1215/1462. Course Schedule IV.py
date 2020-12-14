# There are a total of n courses you have to take, labeled from 0 to n-1

# Some courses may have direct prerequisites, for example,
# to take course 0 you have first to take course 1,
# which is expressed as a pair: [1,0]
# 코스 0을 타기 위해선 코스 1을 먼저 타야함.

# Given the total number of courses n,
# a list of direct prerequisite pairs and a list of queries pairs.
# 3개의 데이터가 주어짐

# You should answer for each queries[i]
# whether the course queries[i][0] is a prerequisite of the course queries[i][1] or not.
#

# Return a list of boolean, the answers to the given queries.
# 각 쿼리별 응답을 담은 리스트로 리턴
class Solution(object):
    # 그래프 문제
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """



print(Solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]))
# [false, true]
print(Solution.checkIfPrerequisite(2, [], [[0, 1], [1, 0]]))
# [false, false]

# Input: n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
# Output: [true,true]

# Input: n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
# Output: [false,true]

# Input: n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
# Output: [true,false,true,false]
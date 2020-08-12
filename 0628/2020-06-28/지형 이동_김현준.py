from heapq import heappush, heappop
def solution(land, height):
    answer = 0
    N = len(land)
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    costs = [[10000]*N for _ in range(N)]
    costs[0][0] = 0
    v = [[0]*N for _ in range(N)]
    q = []
    # 우선순위 큐 [비용, i, j]
    heappush(q, [0, 0, 0])
    # 프림 알고리즘
    while q:
        cost, i, j = heappop(q)
        if not v[i][j]:
            v[i][j] = 1
            answer += cost
            for d in range(4):
                ni, nj = i+di[d], j+dj[d]
                if 0<=ni<N and 0<=nj<N:
                    cost = abs(land[i][j]-land[ni][nj])
                    if cost <= height:
                        cost = 0
                    if costs[ni][nj] > cost:
                        costs[ni][nj] = cost
                        heappush(q, [cost, ni, nj])
    return answer

# land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
# height = 3
# # result = 15

land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
height = 1
# result = 18

print(solution(land, height))
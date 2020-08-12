import heapq

def solution(land, height):
    N = len(land)
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    group = [[0]*N for _ in range(N)]
    price = [[2**31-1]*N for _ in range(N)]
    ans, Q = 0, []
    heapq.heappush(Q, [0, 0, 0])
    price[0][0] = 0
    while Q:
        diff, r, c = heapq.heappop(Q)
        if group[r][c]: continue
        group[r][c] = 1
        ans += diff
        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                diff = abs(land[nr][nc] - land[r][c])
                if diff <= height: diff = 0
                if price[nr][nc] > diff:
                    price[nr][nc] = diff
                    heapq.heappush(Q, [diff, nr, nc])
    return ans

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3))
# 15
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1))
# 18
from collections import defaultdict
from collections import deque


def find_set(x, p):
    if x == p[x]:
        return x
    else:
        p[x] = find_set(p[x], p)
        return p[x]

def union(x, y, p):
    p[find_set(x, p)] = find_set(y, p)


def bfs(x, y, n, land, height, group, cnt):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = deque()
    q.append((x, y))
    group[x][y] = cnt
    while q:
        x_, y_ = q.popleft()
        for k in range(4):
            nx, ny = x_+di[k], y_+dj[k]
            if 0 <= nx < n and 0 <= ny < n and not group[nx][ny] and abs(land[nx][ny]-land[x_][y_]) <= height:
                group[nx][ny] = cnt
                q.append((nx, ny))

def solution(land, height):
    n = len(land)
    group = [[0] * n for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(n):
            if not group[i][j]:
                bfs(i, j, n, land, height, group, cnt)
                cnt += 1

    adj = defaultdict(lambda: float('inf'))
    for i in range(n):
        for j in range(n):
            if i+1 < n and group[i][j] != group[i+1][j]:
                x, y = min(group[i][j], group[i+1][j]), max(group[i][j], group[i+1][j])
                tmp = abs(land[i][j] - land[i+1][j])
                if adj[(x, y)] > tmp:
                    adj[(x, y)] = tmp
            if j+1 < n and group[i][j] != group[i][j+1]:
                x, y = min(group[i][j], group[i][j+1]), max(group[i][j], group[i][j+1])
                tmp = abs(land[i][j] - land[i][j+1])
                if adj[(x, y)] > tmp:
                    adj[(x, y)] = tmp
    adj = sorted(adj.items(), key=lambda x: x[1])

    answer = 0
    chain = 0
    p = {i:i for i in range(cnt)}
    for el in adj:
        node, minV = el
        node_x, node_y = node
        if find_set(node_x, p) != find_set(node_y, p):
            union(node_x, node_y, p)
            chain += 1
            answer += minV
            if chain == cnt-1:
                break
    return answer

# heapq
import heapq

def solution(land, height):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    answer = 0
    n = len(land)
    costs = [[10000] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    hq = []
    heapq.heappush(hq, [0, 0, 0])
    costs[0][0] = 0
    while hq:
        cost, x, y = heapq.heappop(hq)
        if visited[x][y]: continue
        visited[x][y] = 1
        answer += costs[x][y]
        for k in range(4):
            nx, ny = x+di[k], y+dj[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                tmp = abs(land[x][y]-land[nx][ny])
                if tmp <= height:
                    tmp = 0
                if costs[nx][ny] > tmp:
                    costs[nx][ny] = tmp
                    heapq.heappush(hq, [tmp, nx, ny])
    return answer





land = [[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]
height = 3
print(solution(land, height))

land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
height = 1
print(solution(land, height))
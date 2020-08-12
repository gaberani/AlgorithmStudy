import heapq
def solution(land, height):
    INF, n = float('inf'), len(land)
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    land = [[0]*(n+2)] + [[0]+land[i]+[0] for i in range(n)] + [[0]*(n+2)]
    visited = [[0]*(n+2) for _ in range(n+2)]
    cnt = 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if visited[i][j] == 0:
                visited[i][j] = cnt
                q = [(i, j)]
                while q:
                    x, y = q.pop(0)
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        if visited[nx][ny] == 0 and land[nx][ny] and abs(land[nx][ny] - land[x][y]) <= height:
                            visited[nx][ny] = cnt
                            q.append((nx, ny))
                cnt += 1
    adj = {i:[] for i in range(cnt-1)}
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                value = abs(land[nx][ny] - land[i][j])
                if land[nx][ny] and visited[nx][ny] != visited[i][j] and (visited[nx][ny]-1, value) not in adj[visited[i][j]-1]:
                    adj[visited[i][j]-1].append((visited[nx][ny]-1, value))
    visite = [0] * (cnt-1)
    length, hq = 0, [(0, 0)]
    while hq:
        weight, node = heapq.heappop(hq)
        if visite[node]: continue
        visite[node] = 1
        length += weight
        for n, w in adj[node]:
            if visite[n] == 0:
                heapq.heappush(hq, (w, n))
    return length

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],	3))
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]],	1))
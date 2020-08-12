import sys; input = sys.stdin.readline
from collections import deque


def arrive_bfs(x, y, dest_x, dest_y, fuel):
    global di, dj, start
    q = deque()
    q.append((x, y, fuel, 0))
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    while q:
        x_, y_, fuel_, dist = q.popleft()
        if x_ == dest_x and y_ == dest_y:
            return 1, x_, y_, fuel_+dist*2
        elif not fuel_:
            break

        for k in range(4):
            nx = x_ + di[k]
            ny = y_ + dj[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and start[nx][ny] != -1:
                visited[nx][ny] = 1
                q.append((nx, ny, fuel_-1, dist+1))
    return 0, 0, 0, 0

def start_bfs(x, y, fuel):
    global di, dj, start
    q = deque()
    q.append((x, y, 0))
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    minV = 10**8
    tmp = []
    while q:
        x_, y_, dist = q.popleft()
        if not fuel-dist: break

        if start[x_][y_] >= 1 and minV >= dist:
            if minV > dist:
                minV = dist
            tmp.append((dist, x_, y_))

        for k in range(4):
            nx = x_ + di[k]
            ny = y_ + dj[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and start[nx][ny] != -1:
                visited[nx][ny] = 1
                q.append((nx, ny, dist+1))
    if tmp:
        tmp = sorted(tmp, key=lambda x: (x[0], x[1], x[2]))
        return tmp[0][1], tmp[0][2], fuel-tmp[0][0]
    return 0, 0, 0


N, M, fuel = map(int, input().split())
start = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if start[i][j]:
            start[i][j] = -1
tx, ty = map(int, input().split())
tx -= 1
ty -= 1
info = {}
for i in range(M):
    a, b, c, d = list(map(int, input().split()))
    start[a-1][b-1] = i+1
    info[i+1] = [c-1, d-1]

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

answer = -1
cnt = 0
for _ in range(M):
    x, y, remain = start_bfs(tx, ty, fuel)
    if remain:
        pivot = start[x][y]
        arr = info[pivot]
        cnt += 1
        start[x][y] = 0
        flag, ax, ay, remain_fuel = arrive_bfs(x, y, arr[0], arr[1], remain)
        if cnt == M:
            answer = remain_fuel
        elif flag:
            tx, ty, fuel = ax, ay, remain_fuel
        else:
            break
    else:
        break
print(answer)
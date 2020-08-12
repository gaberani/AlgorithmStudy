from copy import deepcopy

def game(idx):
    global visit, shark, n, k, direcs, dx, dy, copy_visit
    x, y, d = shark[idx]
    d_list = direcs[idx][d-1]
    for i in range(4):
        nx, ny = x+dx[d_list[i]-1], y+dy[d_list[i]-1]
        if 0<=nx<n and 0<=ny<n and copy_visit[nx][ny][0] == 0:
            if visit[nx][ny][0]: shark[visit[nx][ny][0]] = -1
            visit[nx][ny] = [idx, k+1]
            shark[idx] = [nx, ny, d_list[i]]
            return
    for i in range(4):
        nx, ny = x+dx[d_list[i]-1], y+dy[d_list[i]-1]
        if 0<=nx<n and 0<=ny<n and copy_visit[nx][ny][0] == idx:
            visit[nx][ny] = [idx, k+1]
            shark[idx] = [nx, ny, d_list[i]]
            return
    shark[idx] = -1

n, m, k = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
shark = [[0] * 3 for _ in range(m+1)]
visit = [[[0]*2 for _ in range(n)] for _ in range(n)]

for i in range(n):
    input_arr = list(map(int, input().split()))
    for j in range(n):
        if input_arr[j]:
            shark[input_arr[j]][:2] = [i, j]
            visit[i][j][:2] = [input_arr[j], k]

idx = 1
for d in list(map(int, input().split())):
    shark[idx][2] = d
    idx += 1

direcs = [0]
for _ in range(m):
    direc = []
    for _ in range(4):
        direc.append(list(map(int, input().split())))
    direcs.append(deepcopy(direc))

for t in range(1, 1001):
    copy_visit = deepcopy(visit)
    for i in range(m, 0, -1):
        if shark[i] != -1:
            game(i)
    for i in range(n):
        for j in range(n):
            if visit[i][j][0]:
                visit[i][j][1] -= 1
                if visit[i][j][1] == 0: visit[i][j][0] = 0
    for i in range(m, 1, -1):
        if shark[i] != -1: break
    else:
        print(t)
        break
else: print(-1)
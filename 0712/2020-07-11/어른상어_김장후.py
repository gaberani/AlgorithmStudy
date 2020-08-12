import sys; input = sys.stdin.readline


def check(x, y, s_dir):
    global ocean, smell, priority, di, dj
    cx, cy, ck, mx, my, mk = 0, 0, 0, 0, 0, 0
    possible_smell = []
    possible_me = []
    cnt, me = 0, 0
    for k in range(1, 5):
        nx = x + di[k]
        ny = y + dj[k]
        if 0 <= nx < N and 0 <= ny < N:
            if not smell[nx][ny]:
                cnt += 1
                possible_smell.append(k)
                cx, cy, ck = nx, ny, k
            elif ocean[nx][ny] == ocean[x][y]:
                me += 1
                mx, my, mk = nx, ny, k
                possible_me.append(k)

    if cnt == 1:
        # 아무도 없는 칸
        return cx, cy, ck
    elif not cnt and me == 1:
        # 기존 본인 방향
        return mx, my, mk
    else:
        # 우선순위
        arr = priority[ocean[x][y]][s_dir-1]
        for idx in arr:
            if idx in possible_smell:
                return x+di[idx], y+dj[idx], idx

        for idx in arr:
            if idx in possible_me:
                return x+di[idx], y+dj[idx], idx







# base setting
N, M, k = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(N)]
smell = [[0] * N for _ in range(N)]
shark_info = {i+1: [] for i in range(M)}
answer = -1
for i in range(N):
    for j in range(N):
        if ocean[i][j]:
            shark_info[ocean[i][j]].append(i)
            shark_info[ocean[i][j]].append(j)
            smell[i][j] = k
shark_dir = list(map(int, input().split()))
for i in range(M):
    shark_info[i+1].append(shark_dir[i])

priority = {i+1: [] for i in range(M)}
for num in priority:
    for _ in range(4):
        priority[num].append(list(map(int, input().split())))
di = [0, -1, 1, 0, 0] # 위, 아래, 왼쪽, 오른쪽
dj = [0, 0, 0, -1, 1]

time = 0
while time < 1000:
    time += 1
    tmp = [[0] * N for _ in range(N)]
    for key, value in shark_info.items():
        if value:
            si, sj, s_dir = value
            if ocean[si][sj]:
                x, y, dir_ = check(si, sj, s_dir)
                if tmp[x][y]:
                    shark_info[key] = 0
                else:
                    tmp[x][y] = ocean[si][sj]
                    value[0], value[1], value[2] = x, y, dir_
    shark = 0
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j] -= 1
                if not smell[i][j]:
                    ocean[i][j] = 0
            if tmp[i][j]:
                smell[i][j] = k
                ocean[i][j] = tmp[i][j]
                shark += 1
    if shark == 1:
        answer = time
        break
print(answer)
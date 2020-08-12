# 2.
import sys; input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
room[r][c] = 2
di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

if d == 1:
    d = 3
elif d == 3:
    d = 1

cnt = 1
while True:
    for k in range(4):
        nr = r + di[(d+k+1)%4]
        nc = c + dj[(d+k+1)%4]
        if not room[nr][nc]:
            room[nr][nc] = 2
            r, c, d = nr, nc, (d+k+1)%4
            cnt += 1
            break
    else:
        k_ = (d+2)%4
        r += di[k_]
        c += dj[k_]
        if room[r][c] == 1:
            break
print(cnt)

# 1.
import sys
from collections import deque

def dfs(x, y):
    global d, area
    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]
    if d == 1: # 방향 값 변환: 문제 -> (0, 1, 2, 3), 내 기준 -> (0, 3, 2, 1)
        d = 3
    elif d == 3:
        d = 1
    stack = deque()
    stack.append((x, y, 1, d)) # 청소한 구역과 바라보고 있는 방향을 함께 저장
    area[x][y] = 2 # 청소 구역 표시
    while stack:
        t, s, cnt, dic = stack.pop()
        for k in range(dic+1, dic+4+1): # 왼쪽부터 탐색
            ni = t + di[k%4]
            nj = s + dj[k%4]
            if 0 <= ni < N and 0 <= nj < M and area[ni][nj] == 0: # 청소할 수 있으면
                area[ni][nj] = 2
                stack.append((ni, nj, cnt+1, k%4)) # 현재 바라보고 있는 방향 저장
                break
        else: # 전부 돌았는데 없다면
            t -= di[dic] # 후진
            s -= dj[dic]
            if area[t][s] == 1: # 후진 했을 때 벽이면 break
                return cnt
            stack.append((t, s, cnt, dic)) # 아니면 다시 탐색하기 위해 stack에 저장
    return cnt

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = dfs(r, c)
print(answer)
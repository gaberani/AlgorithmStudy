import sys
from collections import deque

# 재귀
def bfs(x):
    global info_virus, maxV
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    cnt = 0
    queue = deque()
    for virus in info_virus:
        queue.append(virus)
    while queue:
        t, s = queue.popleft()
        for k in range(4):
            ni = t + di[k]
            nj = s + dj[k]
            if 0 <= ni < N and 0 <= nj < M and x[ni][nj] == 0:
                x[ni][nj] = 2
                queue.append((ni, nj))

    for i in range(N):
        for j in range(M):
            if x[i][j] == 0:
                cnt += 1
    if maxV < cnt:
        maxV = cnt
    return maxV

def dfs(cnt):
    global area
    if cnt == 3:
        rnd2 = [[0] * M for _ in range(N)] # 벽의 갯수가 3이 되면 리스트 복사 후
        for i in range(N):
            for j in range(M):
                rnd2[i][j] = rnd[i][j]
        bfs(rnd2) # 바이러스 퍼트리는 작업은 bfs로
        return
    else:
        for i in range(N):
            for j in range(M):
                if rnd[i][j] == 0 and area[i][j] == 0:
                    area[i][j] = 1
                    rnd[i][j] = 1
                    dfs(cnt+1)
                    area[i][j] = 0
                    rnd[i][j] = 0

N, M = map(int, sys.stdin.readline().split())
rnd = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
area = [[0] * M for _ in range(N)]
info_virus = []
maxV = 0
for i in range(N):
    for j in range(M):
        if rnd[i][j] == 2: # 바이러스 정보 저장
            info_virus.append((i, j))
dfs(0) # 모든 경우의 수 확인
print(maxV)


# mod 연산
import sys
from collections import deque

def bfs(x):
    global virus_info, answer
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = deque()
    for virus in virus_info:
        q.append(virus)
    while q:
        t, s = q.popleft()
        for k in range(4):
            ni = t + di[k]
            nj = s + dj[k]
            if 0 <= ni < N and 0 <= nj < M and x[ni][nj] == 0:
                x[ni][nj] = 2
                q.append((ni, nj))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if x[i][j] == 0:
                cnt += 1
    if answer < cnt:
        answer = cnt

N, M = map(int, sys.stdin.readline().split())
rnd = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
virus_info = []
answer = 0
for i in range(N):
    for j in range(M):
        if rnd[i][j] == 2:
            virus_info.append((i, j))

for i in range(N*M-2):
    if rnd[i//M][i%M] == 0:
        for j in range(i+1, N*M-1):
            if rnd[j//M][j%M] == 0:
                for k in range(j+1, N*M):
                    if rnd[k//M][k%M] == 0:
                        tmp = [[0] * M for _ in range(N)]
                        for t in range(N):
                            for s in range(M):
                                tmp[t][s] = rnd[t][s]
                        tmp[i//M][i%M] = 1
                        tmp[j//M][j%M] = 1
                        tmp[k//M][k%M] = 1
                        bfs(tmp)
print(answer)
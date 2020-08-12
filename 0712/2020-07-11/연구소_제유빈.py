# 연구소 다시풀기
import sys
from copy import deepcopy
from collections import deque

# 벽을 세개 세운다.
def wall(i, r):
    global N, M
    if i == 3:
        # 벽을 세운 후 바이러스를 퍼트린다.
        infect(deepcopy(P))
        return
    else:
        # 다음에 세울 벽을 찾는다.
        # 이전에 벽을 세운 행에서 시작
        for row in range(r, N):
            for col in range(M):
                # 비어있으면 벽을 놓는다.
                if not P[row][col]:
                    P[row][col] = 1
                    wall(i+1, row)
                    P[row][col] = 0

# 바이러스 퍼트리기
def infect(p):
    global max_total
    # 4방향
    dr, dc = [1, 0, 0, -1], [0, 1, -1, 0]
    # 바이러스 좌표 배열 복사
    V = deepcopy(virus)
    while V:
        r, c = V.popleft()
        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            # 배열 안에 있고 비어있는 공간이면 퍼트린다.
            if 0 <= nr < N and 0 <= nc < M and not p[nr][nc]:
                p[nr][nc] = 2
                # 이동한 지점을 기준점으로 삼기 위해 새로 저장
                V.append((nr, nc))

    # 안전 영역 크기 찾기
    total = 0
    for r in range(N):
        total += p[r].count(0)
    # 안전 영역이 최댓값인 경우 저장
    if total > max_total: max_total = total


N, M = map(int, sys.stdin.readline().split())
P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_total = 0

# 바이러스 좌표 저장
virus = deque()
for i in range(N):
    for j in range(M):
        if P[i][j] == 2:
            virus.append((i, j))

wall(0, 0)
print(max_total)


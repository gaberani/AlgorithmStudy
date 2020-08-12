#        위  아  왼  오
di = [0, -1,  1,  0, 0]
dj = [0,  0,  0, -1, 1]
import pprint

# N: 줄, M: 상어 마리수, K: 냄새 남아있는 시간
N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
smell_grid = [[[0, 0] for _ in range(N)] for _ in range(N)]
sang_P = {}
sang_D = {}
sang_D_input = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            # 상어 찾아서 dict 등록 / smell_grid에 [sang_num, K] 로 등록
            sang_P[grid[i][j]] = [i, j]
            sang_D[grid[i][j]] = [sang_D_input[grid[i][j] - 1]]
            smell_grid[i][j] = [grid[i][j], K]

# 상어별 기본 방향에 따른 방향우선순위 정리
for m in range(M*4):
    sang_D[m//4+1].append(list(map(int, input().split())))
# print(sang_P)   # 상어의 위치
# print(sang_D)   # 상어의 방향, 방향에 따른 우선순위
# pprint.pprint(grid)
# print('----------------')

# 각 상어 이동 방향대로 이동시키기
def move(si, sj):
    sang_KEY = grid[si][sj]
    now_D = sang_D[sang_KEY][0]
    # 1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향
    flag = 0
    for d in sang_D[sang_KEY][now_D]:
        ni, nj = si+di[d], sj+dj[d]
        if 0 <= ni < N and 0 <= nj < N:
            # 냄새 없는곳 저장
            if smell_grid[ni][nj][1] == 0:
                # print(sang_KEY, d)
                sang_D[sang_KEY][0] = d
                sang_P[sang_KEY] = [ni, nj]
                flag = 1
                break

    # 2. 냄새 없는 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
    if not flag:
        for d in sang_D[sang_KEY][now_D]:
            ni, nj = si+di[d], sj+dj[d]
            if 0 <= ni < N and 0 <= nj < N:
                if smell_grid[ni][nj][0] == sang_KEY:
                    sang_D[sang_KEY][0] = d
                    sang_P[sang_KEY] = [ni, nj]
                    break
    # 3. 이때 가능한 칸이 여러 개이면, 그 경우에는 특정한 우선순위를 따른다.
    grid[si][sj] = 0

# 냄새 제거 & 새로 상어가 자리잡은 자리 냄새 갱신
def smell():
    # 남아있는 냄새들 -1씩
    for i in range(N):
        for j in range(N):
            if smell_grid[i][j][1]:
                smell_grid[i][j][1] -= 1
                # 빼서 냄새가 사라지는 순간이면 번호도 지우기
                if smell_grid[i][j][1] == 0:
                    smell_grid[i][j][0] = 0

    # 남은 상어들 냄새 K초 남기기
    for sid in range(1, M+1):
        if sid in sang_P:
            si, sj = sang_P[sid]
            smell_grid[si][sj] = [grid[si][sj], K]


# 1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다.
t = 0
while len(sang_P) > 1:
    # 모든 상어 이동시킴
    for num in range(1, M+1):
        if num in sang_P:
            si, sj = sang_P[num]
            move(si, sj)

    # 새로운 위치 겹치는 상어 있으면 번호 비교 후, 더 큰 상어 숫자를 제거
    # for s in range(1, N+1):
    #     if num in sang_P:
    #         si, sj = sang_P[num]
    for s1 in range(1, M):
        for s2 in range(s1+1, M+1):
            if s1 in sang_P and s2 in sang_P:
                si1, sj1 = sang_P[s1]
                si2, sj2 = sang_P[s2]
                if si1 == si2 and sj1 == sj2:
                    gt_sang = s1 if s1 > s2 else s2
                    del sang_P[gt_sang]


    for num in range(1, M+1):
        if num in sang_P:
            si, sj = sang_P[num]
            grid[si][sj] = num
    # pprint.pprint(grid)
    # print('----------------')
    # 냄새 -1 & 시간 +1
    smell()
    t += 1
    if t >= 1000:
        break

# 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력
if len(sang_P) > 1:
    t = -1
print(t)
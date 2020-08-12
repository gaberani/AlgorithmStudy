import copy
# 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호
# 가로, 세로
# di = [[[0], [1], [0], [-1]], [[0,  0], [1, -1]], [[-1, 0], [0, 1], [1, 0], [0,-1]], [[-1, 0], [], [], []], [1, 0, -1, 0]]
# dj = [[[1], [0], [-1], [0]], [[1, -1], [0,  0]], [[ 0, 1], [1, 0], [0,-1], [-1,0]], [[], [], [], []], [0, 1, 0, -1]]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if 0 < grid[i][j] < 6:
            cctv.append((i, j))
L = len(cctv)


def dfs(idx, office):
    global minV
    if idx == L:
        V = 0
        for i in range(N):
            V += office[i].count(0)
        minV = min(minV, V)
    else:
        ci, cj = cctv[idx]
        # cctv 종류는 무조건 원본 grid에서 확인
        cctv_num = grid[ci][cj]

        if cctv_num == 1:
            for d in range(4):
                tmp_office = copy.deepcopy(office)
                ni, nj = ci+di[d], cj+dj[d]
                while 0 <= ni < N and 0 <= nj < M and tmp_office[ni][nj] < 6:
                    tmp_office[ni][nj] = cctv_num
                    ni, nj = ni+di[d], nj+dj[d]
                dfs(idx+1, tmp_office)

        elif cctv_num == 2:
            for n in range(2):
                tmp_office = copy.deepcopy(office)
                for d in range(0, 4, 2):
                    ni, nj = ci+di[(n+d)%4], cj+dj[(n+d)%4]
                    while 0 <= ni < N and 0 <= nj < M and tmp_office[ni][nj] != 6:
                        tmp_office[ni][nj] = cctv_num
                        ni, nj = ni+di[(n+d)%4], nj+dj[(n+d)%4]
                dfs(idx+1, tmp_office)

        elif cctv_num == 3:
            for n in range(4):
                tmp_office = copy.deepcopy(office)
                for d in range(2):
                    ni, nj = ci + di[(n+d)%4], cj + dj[(n+d)%4]
                    while 0 <= ni < N and 0 <= nj < M and tmp_office[ni][nj] != 6:
                        tmp_office[ni][nj] = cctv_num
                        ni, nj = ni+di[(n+d)%4], nj+dj[(n+d)%4]
                dfs(idx+1, tmp_office)

        elif cctv_num == 4:
            for n in range(4):
                tmp_office = copy.deepcopy(office)
                for d in range(3):
                    ni, nj = ci + di[(n+d)%4], cj + dj[(n+d)%4]
                    while 0 <= ni < N and 0 <= nj < M and tmp_office[ni][nj] != 6:
                        tmp_office[ni][nj] = cctv_num
                        ni, nj = ni+di[(n+d)%4], nj+dj[(n+d)%4]
                dfs(idx+1, tmp_office)

        elif cctv_num == 5:
            tmp_office = copy.deepcopy(office)
            for d in range(4):
                ni, nj = ci+di[d], cj+dj[d]
                while 0 <= ni < N and 0 <= nj < M and tmp_office[ni][nj] != 6:
                    tmp_office[ni][nj] = cctv_num
                    ni, nj = ni+di[d], nj+dj[d]
            dfs(idx+1, tmp_office)


minV = N*M
dfs(0, grid)
# 사각 지대의 최소 크기를 출력
print(minV)
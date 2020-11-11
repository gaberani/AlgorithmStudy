# 파이어스톰을 크기가 2N × 2N인 격자로 나누어진 얼음판에서 연습하려고 한다.
# 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 얼음의 양을 의미한다.
# A[r][c]가 0인 경우 얼음이 없는 것이다.

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def firestorm(si, sj, cnt):
    for i in range(cnt):
        for j in range(cnt):
            tmp[si+j][sj-i+cnt-1] = grid[si+i][sj+j]
    # for t in tmp: print(t)

def dfs(si, sj):
    global visit, N
    visit[si][sj] = 1
    cnt = 1
    q = [(si, sj)]
    while q:
        i, j = q.pop(0)
        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            if 0 <= ni < 2**N and 0 <= nj < 2**N and not visit[ni][nj] and grid[ni][nj]:
                visit[ni][nj] = 1
                q.append((ni, nj))
                cnt += 1
    return cnt

# 마법사 상어는 파이어스톰을 총 Q번 시전한다. 모든 파이어스톰을 시전 후, 다음 2가지를 구하기
# 1. 남아있는 얼음 A[r][c]의 합
# 2. 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면,
# 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.
N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**N)]
level_lst = list(map(int, input().split()))

# 단계 L을 결정해야 한다.
for L in level_lst:
    tmp = [[0]*(2**N) for _ in range(2**N)]
    # 파이어스톰은 먼저 격자를 2L × 2L 크기의 부분 격자로 나눈다.
    for si in range(0, 2**N, 2**L):
        for sj in range(0, 2**N, 2**L):
            # 그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
            firestorm(si, sj, 2**L)

    # 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
    # (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다.
    remove_ices = []
    for i in range(2**N):
        for j in range(2**N):
            if tmp[i][j] > 0:
                ice_cnt = 0
                for d in range(4):
                    ni, nj = i+di[d], j+dj[d]
                    if 0 <= ni < 2**N and 0 <= nj < 2**N and tmp[ni][nj] > 0:
                        ice_cnt += 1
                if ice_cnt <= 2:
                    remove_ices.append((i, j))

    for remove_ice in remove_ices:
        ri, rj = remove_ice
        tmp[ri][rj] -= 1

    # print('----------------')
    for i in range(2**N):
        for j in range(2**N):
            grid[i][j] = tmp[i][j]
    # for g in grid: print(g)
# 남아있는 얼음 A[r][c]의 합, 가장 큰 덩어리가 차지하는 칸의 개수를 출력
remain_ice = 0
for g in grid: remain_ice += sum(g)

visit = [[0]*(2**N) for _ in range(2**N)]
biggest_ice = 0
for i in range(2**N):
    for j in range(2**N):
        if grid[i][j] and not visit[i][j]:
            biggest_ice = max(biggest_ice, dfs(i, j))

print(remain_ice)
print(biggest_ice)
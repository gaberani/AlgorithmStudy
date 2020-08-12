import heapq

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

# 오늘 M명의 승객을 태우는 것이 목표 / 활동 영역은 N×N 크기의 격자
N, M, F = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ti, tj = map(int, input().split())
guests = [[0] + list(map(int, input().split())) for _ in range(M)]
for guest in guests:
    _i, _j = guest[1] - 1, guest[2] - 1
    grid[_i][_j] = 2

def check():
    for gi in grid:
        if 2 in gi:
            return True
    return False

def move(mi, mj, fuel):
    v = [[0] * N for _ in range(N)]
    # 손님 목적지 좌표 찾기
    for guest in guests:
        if mi == guest[1] - 1 and mj == guest[2] - 1:
            ei, ej = guest[3] - 1, guest[4] - 1
            break

    # 손님 목적지 데려다 주기
    q = []
    q.append([mi, mj, fuel])
    while q:
        i, j, f = q.pop(0)
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] != 1 and v[ni][nj] == 0:
                # 목적지 찾음
                if ni == ei and nj == ej:
                    # 연료 체크 -> 성공
                    if f - 1 > 0:
                        # 이동한 거리 *2 만큼 연료 보충
                        f += (fuel-(f-1))*2-1
                        # 맵에서 손님 지우기
                        grid[mi][mj] = 0
                        if check():
                            return bfs(ni, nj, f)
                        else:
                            return f
                    # 실패
                    else:
                        return -1
                else:
                    q.append([ni, nj, f-1])
                    v[ni][nj] = 1
    # q가 끝날 동안 못찾으면
    return -1

# 손님 찾기
def bfs(bi, bj, fuel):
    visit = [[0] * N for _ in range(N)]
    # 택시가 있는 자리에 손님이 있으면 바로 보내기(최소 거리이므로)
    if grid[bi][bj] == 2:
        return move(bi, bj, fuel)
    # 택시자리에 손님 없으면 손님 찾기 시작
    else:
        q = []
        tmp = []
        h = []
        q.append([bi, bj, fuel])
        while q:
            i, j, f = q.pop(0)
            # distance, i, j = heapq.heappop(q)
            # f = fuel - distance
            if f - 1 > 0:
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        if grid[ni][nj] == 0 and visit[ni][nj] == 0:
                            # heapq.heappush(q, (fuel-(f-1), ni, nj))
                            tmp.append([ni, nj, f-1])
                            visit[ni][nj] = 1
                        # 손님 찾는대로 전부 추가
                        elif grid[ni][nj] == 2 and visit[ni][nj] == 0:
                            heapq.heappush(h, (fuel-(f-1), ni, nj))
            if not q:
                if h:
                    distance, hi, hj = heapq.heappop(h)
                    return move(hi, hj, fuel-distance)
                else:
                    q = tmp
                    tmp = []
        # q도는 동안 손님 못찾으면
        return -1
print(bfs(ti-1, tj-1, F))

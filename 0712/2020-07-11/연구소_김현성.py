di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(lab):
    global maxV
    q = []
    visit = [[0]*M for _ in range(N)]
    # 바이러스 좌표 찾기
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                q.append((i, j))
                visit[i][j] = 1
    # 바이러스 퍼뜨리기
    while len(q) != 0:
        x, y = q.pop(0)
        for k in range(4):
            ni = x + di[k]
            nj = y + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if lab[ni][nj] == 0 and visit[ni][nj] == 0:
                    q.append((ni, nj))
                    visit[ni][nj] = visit[x][y] + 1
    # 안전영역 세기
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0 and visit[i][j] == 0:
                cnt += 1
    # 최대값 갱신
    if maxV < cnt:
        maxV = cnt

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
zero = []

# 0있는 곳 좌표 전부 저장
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zero.append((i, j))
# 조합
L = len(zero)
for n1 in range(L - 2):
    for n2 in range(n1+1, L-1):
        for n3 in range(n2+1, L):
            # 뽑아낸 벽 세우기
            lab[zero[n1][0]][zero[n1][1]] = 1
            lab[zero[n2][0]][zero[n2][1]] = 1
            lab[zero[n3][0]][zero[n3][1]] = 1
            # 안전 영역 체크하기 / 최대값 세기
            bfs(lab)
            # 세운 벽 초기화
            lab[zero[n1][0]][zero[n1][1]] = 0
            lab[zero[n2][0]][zero[n2][1]] = 0
            lab[zero[n3][0]][zero[n3][1]] = 0
print(maxV)
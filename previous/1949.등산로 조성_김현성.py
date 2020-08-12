# 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.
di = [0, 1, 0,-1]
dj = [1, 0,-1, 0] # 동 남 서 북
def down(i, j, cnt, flag):
    global maxV
    si, sj = i, j
    for d in range(4): # 봉우리에서 출발해서 자기보다 작은 곳 4방 탐색
        x = si + di[d]
        y = sj + dj[d]
        if 0 <= x <= N-1 and 0 <= y <= N-1:
            if road[si][sj] > road[x][y] and visit[x][y] == 0:     # 1. 갈 수 있으면 ㄱㄱ
                if flag:
                    visit[x][y] = 1
                    down(x, y, cnt+1, 1)
                    visit[x][y] = 0
                else:
                    visit[x][y] = 1
                    down(x, y, cnt+1, 0)
                    visit[x][y] = 0

            elif not flag:                  # 2. 못가고 공사 안했으면
                for nk in range(1, K+1):          # 막혀있던 곳을 K 범위 안에서 깍아서 등산로 만들기
                    road[x][y] -= nk               # 공사해보고
                    if road[si][sj] > road[x][y] and visit[x][y] == 0:  # 갈 수 있으면 ㄱㄱ
                        visit[x][y] = 1
                        down(x, y, cnt+1, 1)      # 공사했으니깐 flag = 1
                        visit[x][y] = 0
                    road[x][y] += nk
        if maxV < cnt:
            maxV = cnt
# N: 한 변의 길이, K: 최대 공사 깊이
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    bong = 0
    roof = []
    for i in range(N):
        for j in range(N):
            if bong < road[i][j]:
                bong = road[i][j]
                roof = []
                roof.append([i, j])
            elif bong == road[i][j]:
                roof.append([i, j])
    maxV = 0
    visit = [[0]*N for _ in range(N)]
    for s in roof:
        visit[s[0]][s[1]] = 1
        down(s[0], s[1], 1, 0)
        visit[s[0]][s[1]] = 0
    print('#{0} {1}'.format(tc+1, maxV))
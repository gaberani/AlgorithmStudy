di = [-1, 0, 1,  0]
dj = [ 0, 1, 0, -1]  # 북 동 남 서

def clean(dx, dy, d):
    s = []
    c = 0  # 방향 돌때마다 세서 모든 방향을 봐서 없으면 방향 유지해서 후진,
    s.append((dx, dy, d, c))
    while len(s) != 0:
        x, y, sd, c = s.pop()
        room[x][y] = 2      # 회전만 해서 같은 자리여도 2로 갱신이라 상관 없음.
        nd = sd-1
        if nd < 0:
            nd = 3
        nx = x + di[nd]
        ny = y + dj[nd]
        # a. 청소하지 않은 공간이 존재한다면, 그 방향으로 회전 후 한 칸을 전진하고 1번부터 진행
        if room[nx][ny] == 0:
            s.append((nx, ny, nd, 0))
        else:
            if c == 4:                    # 1바퀴 돌았는데 할게 없네?
                lx, ly = x-di[(nd+1)%4], y-dj[(nd+1)%4]
                if room[lx][ly] == 1:       # d. 네 방향 모두 청소,벽 and 벽이라 후진 불가
                    break
                elif room[lx][ly] == 2:     # c. 네 방향 모두 청소,벽 and 2라서 후진 가능
                    s.append((lx, ly, (nd+1)%4, 0))   # 후진 ㄱㄱ
            else:
                s.append((x, y, nd, c+1))   # 벽(1)이나 청소(2)되어있으면 회전만 하고 움직이지 않음


# N: 세로, M: 가로
N, M = map(int, input().split())
Rx, Ry, Rd = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]

clean(Rx, Ry, Rd)
min_D = 0
for i in range(N):
    for j in range(M):
        if room[i][j] == 2:
            min_D += 1
print(min_D)
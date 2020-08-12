di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]  # 우 하 좌 상

def shoot(n, k):
    if n == k:
        # print(shootNum)
        wallshoot(shootNum)
        return
    else:
        for i in range(W):
            shootNum[n] = i
            shoot(n+1, k)

def wallshoot(shootNum):
    global minV
    cnt = 0
    for _ in range(N):
        flag = 1
        i, shoot_j = 0, shootNum[_] # 시작점 설정
        while game[i][shoot_j] == 0:
            i += di[1]
            if i == H:
                flag = 0
                break
        if flag:
            boom(i, shoot_j)

        # 터진 곳을 0으로 만들기
        for _i in range(H):
            for _j in range(W):
                if shootgrid[_i][_j] == 1:
                    game[_i][_j] = shootgrid[_i][_j] = 0
        # 한 번 쏘고 난뒤 밑으로 벽돌 떨어뜨리기
        for _i in range(H-2, -1, -1):     # 밑 줄부터 탐색
            for _j in range(W):
                if game[_i][_j] != 0:
                    _ni, _nj = _i+di[1], _j
                    while game[_ni][_nj] == 0:
                        imsi = game[_ni-di[1]][_nj]
                        game[_ni][_nj] = imsi
                        game[_ni - di[1]][_nj] = 0
                        _ni += di[1]
                        if _ni == H:
                            break
    # shoutNum 다 꺼낸 뒤엔 남은 벽돌(0아닌 것) 세기
    # 동시에, 다음 시도를 위해 돌려 놓기
    for _i in range(H):
        for _j in range(W):
            if game[_i][_j] != 0:
                cnt += 1
            game[_i][_j] = origin_game[_i][_j]
    if minV > cnt:
        minV = cnt

def boom(x, y):
    orix, oriy = x, y
    shootgrid[x][y] = 1
    for nd in range(4):         # 4방향(우 하 좌 상)
        nx = orix
        ny = oriy
        for _ in range(game[x][y] - 1):  # (그 자리 수-1) 만큼 4방향으로 연달아 깨짐
            nx += di[nd]
            ny += dj[nd]
            if 0 <= nx <= H - 1 and 0 <= ny <= W - 1:
                if game[nx][ny] != 0 and shootgrid[nx][ny] != 1:
                    boom(nx, ny)
                # shootgrid[ni][nj] = 0

# 셋팅
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split()) # N번 쏜다, W * H 배열
    origin_game = [list(map(int, input().split())) for _ in range(H)]
    game = [[0]*W for _ in range(H)]
    for _i in range(H):
        for _j in range(W):
            game[_i][_j] = origin_game[_i][_j]
    shootgrid = [[0]*W for _ in range(H)]
    shootNum = [0]*N
    minV = W*H

    shoot(0, N)          # 시작
    print('#{0} {1}'.format(tc+1, minV))
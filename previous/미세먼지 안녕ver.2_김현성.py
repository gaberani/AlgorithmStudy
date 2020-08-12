import pprint

R,C,T = map(int,input().split())
room = [list(map(int, input().split())) for _ in range(R)]
di = [-1,  0, 1, 0]
dj = [ 0, -1, 0, 1]
time = 0
while time < T:
    # 미세먼지 확산
    tmp_R = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                cnt = 0
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        tmp_R[ni][nj] += (room[i][j] // 5)
                        cnt += 1
                room[i][j] = room[i][j] - (room[i][j] // 5) * cnt
    for i in range(R):
        for j in range(C):
            room[i][j] += tmp_R[i][j]

    # 공기청정기 순환시키는 부분
    tmp_R = [[-2] * C for _ in range(R)]
    up = 0
    # 공기청정기 윗부분 찾기
    for i in range(R):
        if room[i][0] == -1:
            up = i
            break

    # 위쪽
    for i in range(1, C):
        tmp_R[0][i-1] = room[0][i]      # 윗줄
        tmp_R[up][i] = room[up][i-1]    # 청정기 줄
        tmp_R[up][1] = 0                # 청정기 자리

    for i in range(1, up+1):
        if room[i][0] != -1:
            tmp_R[i][0] = room[i-1][0]
        tmp_R[i-1][C-1] = room[i][C-1]
    # 아래쪽(up+1)
    for i in range(1, C):
        tmp_R[R-1][i-1] = room[R-1][i]      # 아랫 줄
        tmp_R[up+1][i] = room[up+1][i-1]    # 청정기 줄
        tmp_R[up+1][1] = 0                  # 청정기 자리
    for i in range(up+2, R):
        if room[i-1][0] != -1:
            tmp_R[i-1][0] = room[i][0]
        tmp_R[i][C-1] = room[i-1][C-1]

    for i in range(R):
        for j in range(C):
            if tmp_R[i][j] != -2:
                room[i][j] = tmp_R[i][j]
    # pprint.pprint(tmp_R)
    # pprint.pprint(room)
    # print('-------------------')
    time += 1

result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            result += room[i][j]
print(result)
# print(sum(list(sum(room, []))) + 2)
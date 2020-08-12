di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]  # 오 왼 위 아래


def blue(i, j):
    if 0 <= i < N and 0 <= j < N:
        if color[i][j] == 2:  # 게임판 위치가 파란색일 경우
            return True
        return False
    else:  # 게임판 벗어날 경우
        return True


def move():
    for k in range(K):
        # 좌표 계산
        hi, hj, d = horse[k][0], horse[k][1], horse[k][2]
        ni, nj = hi + di[d], hj + dj[d]  # 일단 d 방향대로 좌표 찍고
        if blue(ni, nj):  # 확인하기
            ni, nj = hi - di[d], hj - dj[d]  # 반대로 이동시킴
            d = 1 if d == 2 else d  # 방향 반대로 맞춰주기
            d = 3 if d == 4 else d  # ''
            if blue(ni, nj):  # 반대로 이동 시킨 곳도 blue라면
                ni, nj = hi, hj  # 처음 자리 유지
        origin_idx = game[hi][hj].index(k)  # 이전 위치에서 높이 찾기
        for n in game[hi][hj][origin_idx:]:  # 그 높이 위로 싹 가져와서
            horse[n][0], horse[n][1] = ni, nj  # 위치 같이 옮겨줌

        # 게임판에 옮기기
        head = game[hi][hj][origin_idx:]  # 윗부분 떼어내기
        game[hi][hj] = game[hi][hj][:origin_idx]  # 아랫부분만 남겨서 저장
        if color[ni][nj] == 0:  # 흰색
            game[ni][nj] += head[:]  # 그대로 붙임
        elif color[ni][nj] == 1:  # 빨간색
            game[ni][nj] += head[::-1]  # 밑에는 유지시켜서 붙임
        if len(game[ni][nj]) >= 4:  # 높이 확인
            return True
    return False


# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.

# N: 체스판의 크기, K: 말의 개수
N, K = map(int, input().split())
# 0: 흰색 / 1: 빨간색 / 2: 파란색
color = [list(map(int, input().split())) for _ in range(N)]
# i, j, d
horse = [list(map(int, input().split())) for _ in range(K)]
game = [[[] for _ in range(N)] for _ in range(N)]

for k in range(K):
    horse[k][0] -= 1  # 값 맞추기
    horse[k][1] -= 1  # ''
    game[horse[k][0]][horse[k][1]].append(k)  # 인덱스를 게임판에 붙임

t = 0
while t <= 1000:
    t += 1
    if t > 1000:
        print(-1)
        break
    if move():
        print(t)
        break
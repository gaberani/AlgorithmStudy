import sys
input = sys.stdin.readline

def change(d):
    if d == 1:
        d = 2
    elif d == 2:
        d = 1
    elif d == 3:
        d = 4
    else:
        d = 3
    return d

def game():
    global N, K, board, piece, onboard
    di = [0, 0, 0, -1, 1]
    dj = [0, 1, -1, 0, 0]
    i = 0
    while i < K:
        x, y, d = piece[i]
        x -= 1
        y -= 1
        nx = x + di[d]
        ny = y + dj[d]
        new = []
        tmp = onboard[x][y]
        # 위에 쌓여있는 말도 함께 이동
        for j in range(len(tmp)):
            if tmp[j] == (i + 1):
                new = tmp[j:]
                tmp = tmp[:j]
                # 밑에 있는 말
                onboard[x][y] = tmp
                break
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in [0, 1]:
            # white
            if board[nx][ny] == 0:
                # 위에 쌓기
                onboard[nx][ny] += new
            # red
            elif board[nx][ny] == 1:
                # 역으로 쌓기
                onboard[nx][ny] += new[::-1]
                # 함께 이동한 말 전부 이동
            for j in range(K):
                if (j + 1) in new:
                    piece[j][0], piece[j][1] = nx + 1, ny + 1
            if len(onboard[nx][ny]) >= 4:
                return 1
        else:
            d = change(d)
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in [0, 1]:
                if board[nx][ny] == 0:
                    onboard[nx][ny] += new
                elif board[nx][ny] == 1:
                    onboard[nx][ny] += new[::-1]
                for j in range(K):
                    if (j + 1) in new:
                        if i == j:
                            piece[j] = [nx + 1, ny + 1, d]
                        else:
                            piece[j][0], piece[j][1] = nx + 1, ny + 1
                if len(onboard[nx][ny]) >= 4:
                    return 1
            else:
                onboard[x][y] += new
                piece[i] = [x + 1, y + 1, d]
        i += 1
    return 0

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
piece = [list(map(int, input().split())) for _ in range(K)]
onboard = [[[] for _ in range(N)] for _ in range(N)]
for i in range(K):
    x = piece[i][0] - 1
    y = piece[i][1] - 1
    onboard[x][y] = [i + 1]
cnt = 1
while cnt <= 1000:
    # turn
    if game():
        break
    cnt += 1
# 1000턴을 넘결 경우 -1
if cnt > 1000:
    cnt = -1
print(cnt)
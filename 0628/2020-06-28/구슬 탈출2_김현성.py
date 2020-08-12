# 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
# 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다.
# 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.

dy = [-1, 0, 1,  0]
dx = [ 0, 1, 0, -1]

    #    i, j
def move(y, x, d):
    ny = y + dy[d]
    nx = x + dx[d]
    cnt = 0
    while arr[ny][nx] == '.':
        cnt += 1
        ny += dy[d]
        nx += dx[d]
    if arr[ny][nx] == 'O':
        return ny, nx, cnt
    else:
        return ny - dy[d], nx - dx[d], cnt


def bfs(Ry, Rx, By, Bx):
    q = [(Ry, Rx, By, Bx)]
    visit[Ry][Rx][By][Bx] = True
    cnt = 1
    while q and cnt <= 10:
        for i in range(len(q)):
            Ry, Rx, By, Bx = q.pop(0)
            for d in range(4):
                nRy, nRx, R_move = move(Ry, Rx, d)
                nBy, nBx, B_move = move(By, Bx, d)

                if arr[nBy][nBx] == 'O':
                    continue
                # 성공
                elif arr[nRy][nRx] == 'O':
                    return cnt
                else:
                    if nRy == nBy and nRx == nBx:
                        if R_move > B_move:
                            nRy -= dy[d]
                            nRx -= dx[d]
                        else:
                            nBy -= dy[d]
                            nBx -= dx[d]

                        if not visit[nRy][nRx][nBy][nBx]:
                            visit[nRy][nRx][nBy][nBx] = True
                            q.append((nRy, nRx, nBy, nBx))
                    else:
                        if not visit[nRy][nRx][nBy][nBx]:
                            visit[nRy][nRx][nBy][nBx] = True
                            q.append((nRy, nRx, nBy, nBx))
        cnt += 1
    return -1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
# 공 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            By = i
            Bx = j
            arr[i][j] = '.'
        elif arr[i][j] == 'R':
            Ry = i
            Rx = j
            arr[i][j] = '.'

print(bfs(Ry, Rx, By, Bx))
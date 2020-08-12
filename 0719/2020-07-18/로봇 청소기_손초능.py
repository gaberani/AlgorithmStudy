import sys
input = sys.stdin.readline

r, c = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
visit = [[0]*c for _ in range(r)]

visit[x][y] = 1
result = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while 1:
    for i in range(4):
        d = (d-1) % 4
        nx, ny = x+dx[d], y+dy[d]
        if visit[nx][ny] == board[nx][ny] == 0:
            visit[nx][ny] = 1
            result += 1
            x, y = nx, ny
            break
    else:
        x, y = x+dx[(d+2)%4], y+dy[(d+2)%4]
        if board[x][y]: break

print(result)
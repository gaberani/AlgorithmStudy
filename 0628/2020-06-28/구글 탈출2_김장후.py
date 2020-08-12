# 2. BFS
import sys; input = sys.stdin.readline
from collections import deque

def move(x, y, di, dj):
    global matrix
    cnt = 0
    while matrix[x+di][y+dj] != '#':
        cnt += 1
        x += di
        y += dj
        if matrix[x][y] == 'O':
            break
    return (x, y, cnt)

def bfs(ri, rj, bi, bj):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    q = deque()
    q.append((ri, rj, bi, bj, 1))
    visited = [(ri, rj, bi, bj)]
    answer = 11
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt > 10:
            break
        for k in range(4):
            nrx, nry, rcnt = move(rx, ry, di[k], dj[k])
            nbx, nby, bcnt = move(bx, by, di[k], dj[k])
            if matrix[nbx][nby] == 'O': continue
            elif matrix[nrx][nry] == 'O':
                answer = cnt
                return answer
            elif nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= di[k]
                    nry -= dj[k]
                else:
                    nbx -= di[k]
                    nby -= dj[k]

            if (nrx, nry, nbx, nby) not in visited:
                visited.append((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt+1))
    return answer


N, M = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
answer = -1
ri, rj, bi, bj = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'R':
            ri, rj = i, j
        elif matrix[i][j] == 'B':
            bi, bj = i, j
cnt = bfs(ri, rj, bi, bj)
if cnt <= 10:
    answer = cnt
print(answer)



# 1.
import sys
from collections import deque
def move(x, y, kx, ky, d):
    while game[x+kx][y+ky] != '#' and game[x][y] != 'O':
        x += kx
        y += ky
        d += 1
    return x, y, d

def bfs(x):
    global q, c
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    answer = -1
    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt >= 10:
            break
        for k in range(4):
            nrx, nry, rd = move(rx, ry, di[k], dj[k], 0)
            nbx, nby, bd = move(bx, by, di[k], dj[k], 0)
            if game[nbx][nby] == 'O':
                continue
            elif game[nrx][nry] == 'O':
                cnt += 1
                answer = cnt
                return answer
            elif nrx == nbx and nry == nby:
                if rd > bd:
                    nrx, nry = nrx-di[k], nry-dj[k]
                else:
                    nbx, nby = nbx-di[k], nby-dj[k]
            if (nrx, nry, nbx, nby) not in c:
                q.append((nrx, nry, nbx, nby, cnt+1))
                c.append((nrx, nry, nbx, nby))
    return answer

N, M = map(int, sys.stdin.readline().split())
game = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
red = [[0] * M for _ in range(N)]
blue = [[0] * M for _ in range(N)]
q = deque()
c = []
for i in range(N):
    for j in range(M):
        if game[i][j] == 'R':
            rxi, ryj = i, j
        elif game[i][j] == 'B':
            bxi, byj = i, j
q.append((rxi, ryj, bxi, byj, 0))
c.append((rxi, ryj, bxi, byj))
print(bfs(game))
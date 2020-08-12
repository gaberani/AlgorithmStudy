dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# mode == 1 >> 목적지 찾기
# mode == 0 >> 손님 찾기
def bfs(mode, x, y, dest_x, dest_y):
    global board, n, m, dx, dy, find, taxi
    visit = [[1]*(n+2)] + [[1] + [0]*n + [1] for _ in range(n)] + [[1]*(n+2)]
    visit[x][y] = 1
    q = [(x, y, 0)]
    length = 401
    while q:
        x, y, l = q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if board[nx][ny] != 1 and visit[nx][ny] == 0 and l+1 <= length:
                if mode and nx == dest_x and ny == dest_y: return l+1
                if not mode and board[nx][ny] > 1:
                    length, dest_x, dest_y = min((length, dest_x, dest_y), (l+1, nx, ny))
                visit[nx][ny] = 1
                q.append((nx, ny, l+1))
    if length != 401:
        find = board[dest_x][dest_y]-2
        board[dest_x][dest_y] = 0
        return length
    return -1

# input
n, m, energy = map(int, input().split())
board = [[1]*(n+2) for _ in range(n+2)]
for i in range(1, n+1):
    board[i][1:n+1] = list(map(int, input().split()))
taxi = list(map(int, input().split()))
customer = []
flag = find = 1
for i in range(2, m+2):
    x, y, dest_x, dest_y = map(int, input().split())
    from_to = bfs(1, x, y, dest_x, dest_y)
    if from_to == -1:
        flag = 0
        break
    board[x][y] = i
    customer.append((dest_x, dest_y, from_to))

# 시뮬레이션 시작
if flag:
    for t in range(m):
        if board[taxi[0]][taxi[1]] > 1:
            find = board[taxi[0]][taxi[1]]-2
            board[taxi[0]][taxi[1]] = 0
            l = 0
        else:
            l = bfs(0, taxi[0], taxi[1], n+1, n+1)
        if l == -1:
            flag = 0
            break
        energy -= l+customer[find][2]
        if energy < 0:
            flag = 0
            break
        energy += 2*customer[find][2]
        taxi = customer[find][:2]
        customer[find] = -1

if flag: print(energy)
else: print(-1)
import pprint
di = [0, 1,  0, -1]
dj = [1, 0, -1,  0]

# 붐!!
def boom(i, j):
    global b_flag
    s = []
    v = [[0] * 6 for _ in range(12)]
    cnt = 1
    v[i][j] = 1
    s.append((i, j))
    while len(s) != 0:
        x, y = s.pop()
        for k in range(4):
            nx, ny = x+di[k], y+dj[k]
            if 0 <= nx <= 11 and 0 <= ny <= 5:
                if puyo[nx][ny] == puyo[x][y] and not v[nx][ny]:
                    v[nx][ny] = 1
                    s.append((nx, ny))
                    cnt += 1
    if cnt >= 4:
        for i in range(12):
            for j in range(6):
                puyo[i][j] = '.' if v[i][j] else puyo[i][j]
        b_flag = 1

# 현준이식 밀어내기
def down():
    for j in range(6):
        for i in range(11, 0, -1):
            if puyo[i][j] == '.':
                for k in range(i-1, -1, -1):
                    if puyo[k][j] != '.':
                        puyo[i][j], puyo[k][j] = puyo[k][j], puyo[i][j]
                        break

puyo = [list(input()) for _ in range(12)]
pre_result = -1
result = 0
flag = 1
while 1:
    b_flag = 0
    for i in range(11, -1, -1):
        for j in range(6):
            if puyo[i][j] != '.':
                boom(i, j)
    if b_flag:
        result += 1
        down()
    if pre_result == result:
        break
    pre_result = result
print(result)
from copy import deepcopy

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def game():
    global r, c, arr, dx, dy, max_area
    copy_arr = deepcopy(arr)
    q = []
    for i in range(r*c):
        if arr[i//c][i%c] == 2:
            q.append((i//c, i%c))
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<r and 0<=ny<c and copy_arr[nx][ny] == 0:
                copy_arr[nx][ny] = 2
                q.append((nx, ny))
    count = 0
    for i in range(r*c):
        if copy_arr[i//c][i%c] == 0:
            count += 1
    max_area = max(max_area, count)

r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
max_area = 0
for i in range(r*c):
    if arr[i//c][i%c] == 0:
        arr[i//c][i%c] = 1
        for j in range(i+1, r*c):
            if arr[j//c][j%c] == 0:
                arr[j//c][j%c] = 1
                for k in range(j+1, r*c):
                    if arr[k//c][k%c] == 0:
                        arr[k//c][k%c] = 1
                        game()
                        arr[k//c][k%c] = 0
                arr[j//c][j%c] = 0
        arr[i//c][i%c] = 0
print(max_area)
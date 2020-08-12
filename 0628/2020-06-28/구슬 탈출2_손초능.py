def dfs(cnt, red, blue, d):
    global min_value, dx, dy, arr
    if cnt >= min_value: return
    for i in range(4):
        if i == d: continue
        rflag, rlen, r = find(red, i)
        bflag, blen, b = find(blue, i)
        if bflag: continue
        elif rflag:
            min_value = min(min_value, cnt + 1)
            return
        else:
            if r == b:
                if rlen > blen: dfs(cnt+1, [r[0]-dx[i], r[1]-dy[i]], b[:], i)
                else: dfs(cnt+1, r[:], [b[0]-dx[i], b[1]-dy[i]], i)
            else: dfs(cnt+1, r[:], b[:], i)

def find(p, d):
    global arr, dy, dx
    np, cnt, flag = p[:], 0, 0
    while arr[np[0]][np[1]] == '.':
        np[0] += dx[d]
        np[1] += dy[d]
        cnt += 1
    if arr[np[0]][np[1]] == 'O': return 1, cnt, [np[0], np[1]]
    return 0, cnt - 1, [np[0]-dx[d], np[1]-dy[d]]

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'B':
            blue = [i, j]
            arr[i][j] = '.'
        elif arr[i][j] == 'R':
            red = [i, j]
            arr[i][j] = '.'
min_value = 11
dfs(0, red, blue, -1)
if min_value != 11: print(min_value)
else: print(-1)
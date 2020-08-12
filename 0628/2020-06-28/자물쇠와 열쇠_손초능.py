def solution(key, lock):
    n, m, keys, holes = len(lock), len(key), [], 0
    for i in range(m):
        for j in range(m):
            if key[i][j]: keys.append([i, j])
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0: holes += 1
    def turn():
        nonlocal keys, m
        n = len(keys)
        for i in range(n):
            keys[i][0], keys[i][1] = keys[i][1], m-1 - keys[i][0]
    def find():
        nonlocal keys, lock, n, holes, m
        for i in range(n+m-1):
            for j in range(n+m-1):
                cnt, flag = 0, 1
                for k in range(len(keys)):
                    x, y = keys[k][0]-m+1+i, keys[k][1]-m+1+j
                    if 0 <= x < n and 0 <= y < n:
                        if lock[x][y] == 0: cnt += 1
                        else: flag = 0; break
                if cnt == holes and flag: return 1
        return 0
    for _ in range(4):
        if find(): return True
        turn()
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
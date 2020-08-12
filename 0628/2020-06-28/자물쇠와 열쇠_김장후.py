def check(key, full, a, b, unlock, M):
    flag = 0
    for i in range(M):
        for j in range(M):
            if key[i][j]:
                # 만약 key의 돌기와 자물쇠의 돌기가 만나면 종료
                if full[i+a][j+b] == 1:
                    flag = 1
                    break
                # key의 돌기가 자물쇠 홈과 맞으면 unlock - 1
                elif not full[i+a][j+b]:
                    unlock -= 1
        if flag:
            break
    # flag가 표시되어있거나, unlock이 남아있으면 False
    if flag or unlock:
        return 0
    # 아니면 True
    return 1

def rotate(M, key):
    tmp = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            tmp[i][j] = key[M-1-j][i]
    return tmp

def solution(key, lock):
    answer = True
    M, N = len(key), len(lock)
    flag = 0
    unlock = 0
    full = []
    # find unlock
    for i in range(N):
        for j in range(N):
            if not lock[i][j]:
                unlock += 1
    # adjustment
    change = M-1
    # padding
    for arr in lock:
        arr = [2] * change + arr + [2] * change
        full.append(arr)
    full = [[2] * (N+2*change)] * change + full + [[2] * (N+2*change)] * change

    # rotate key
    for rotation in range(4):
        if rotation:
            key = rotate(M, key)
        # search
        for x in range(N+change*2-M+1):
            for y in range(N+change*2-M+1):
                # check
                if check(key, full, x, y, unlock, M):
                    flag = 1
                    break
            if flag:
                break
        if flag:
            break
    else:
        answer = False
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
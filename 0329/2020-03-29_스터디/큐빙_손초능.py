import sys, copy
def rot(s):
    global arr
    if s == 'U': num = 0
    elif s == 'D': num = 1
    elif s == 'F': num = 2
    elif s == 'B': num = 3
    elif s == 'R': num = 4
    elif s == 'L': num = 5
    adj = [ # main 면에 인접하는 면들을 시계방향으로 목록화함
        [3, 4, 2, 5], [2, 4, 3, 5],
        [4, 1, 5, 0], [5, 1, 4, 0],
        [0, 3, 1, 2], [1, 3, 0, 2],
    ]
    touch = [ # main 면에 인접하는 면들의 모서리를 목록화함
        [2, 0, 0, 2], [2, 2, 0, 0], [2, 0, 0, 2],
        [2, 2, 0, 0], [2, 2, 0, 0], [2, 0, 0, 2],
    ]
    copy_arr = [[0]*3 for _ in range(3)]
    for i in range(3): # main 면을 회전
        for j in range(3):
            if num in (1, 3, 4): copy_arr[i][j] = arr[num][j][2-i]
            else: copy_arr[i][j] = arr[num][2-j][i]
    arr[num] = copy.deepcopy(copy_arr)
    temp = arr[adj[num][3]][touch[num][3]][:]
    for i in range(4): # 인접 면들의 모서리를 회전
        x, y, temp_a = adj[num][i], touch[num][i], [0] * 3
        for j in range(3):
            if i % 2:
                temp_a[j] = arr[x][y][j]
                arr[x][y][j] = temp[j]
            else:
                temp_a[j] = arr[x][j][y]
                arr[x][j][y] = temp[j]
        temp = temp_a[:]

T = int(sys.stdin.readline())
for _ in range(T):
    arr = [
        [['w' for _ in range(3)] for _ in range(3)],
        [['y' for _ in range(3)] for _ in range(3)],
        [['r' for _ in range(3)] for _ in range(3)],
        [['o' for _ in range(3)] for _ in range(3)],
        [['b' for _ in range(3)] for _ in range(3)],
        [['g' for _ in range(3)] for _ in range(3)]
    ]  # 윗 면, 아랫 면, 앞 면, 뒷 면, 오른쪽 면, 왼쪽 면
    cnt = int(sys.stdin.readline())
    str_list = list(map(str, sys.stdin.readline().split()))
    for i in range(cnt):
        side, d = map(str, str_list[i])
        if d == '+':
            rot(side)
        else:
            for _ in range(3):
                rot(side)
    for i in range(3):
        print(''.join(arr[0][i]))
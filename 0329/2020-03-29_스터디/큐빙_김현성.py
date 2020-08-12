from copy import deepcopy
import pprint

def clockwise(arr):  # 시계방향으로 회전
    tmp = arr[0][0]
    arr[0][0], arr[2][0], arr[2][2] = arr[2][0], arr[2][2], arr[0][2]
    arr[0][2] = tmp

    tmp = arr[0][1]
    arr[0][1], arr[1][0], arr[2][1]= arr[1][0], arr[2][1], arr[1][2],
    arr[1][2] = tmp

def up(c):
    if c == '+':    # 시계
        k = 1
    else:           # 반시계
        k = 3
    for _ in range(k):
        clockwise(cube[0])
        tmp = cube[1][0][0], cube[1][0][1], cube[1][0][2]
        cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
        cube[4][2][0], cube[4][1][0], cube[4][0][0] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
        cube[5][2][2], cube[5][2][1], cube[5][2][0] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = tmp


def down(c):
    if c == '+':    # 시계
        k = 1
    else:           # 반시계
        k = 3
    for _ in range(k):
        clockwise(cube[2])
        tmp = cube[4][0][2], cube[4][1][2], cube[4][2][2]
        cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]
        cube[1][2][2], cube[1][2][1], cube[1][2][0] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
        cube[5][0][0], cube[5][0][1], cube[5][0][2] = tmp

def right(c):
    if c == '+':    # 시계
        k = 1
    else:           # 반시계
        k = 3
    for _ in range(k):
        clockwise(cube[4])
        tmp = cube[0][0][2], cube[0][1][2], cube[0][2][2]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = tmp

def left(c):
    if c == '+':    # 시계
        k = 1
    else:           # 반시계
        k = 3
    for _ in range(k):
        clockwise(cube[3])
        tmp = cube[0][0][0], cube[0][1][0], cube[0][2][0]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = tmp


def forward(c):
    if c == '+':    # 시계
        k = 1
    else:           # 반시계
        k = 3
    for _ in range(k):
        clockwise(cube[1])
        tmp = cube[0][2][0], cube[0][2][1], cube[0][2][2]
        cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]
        cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[2][0][2], cube[2][0][1], cube[2][0][0]
        cube[2][0][2], cube[2][0][1], cube[2][0][0] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
        cube[4][2][0], cube[4][2][1], cube[4][2][2] = tmp


def backward(c):
    if c == '+':    # 시계
        k = 1
    else:           # 반시계
        k = 3
    for _ in range(k):
        clockwise(cube[5])
        tmp = cube[0][0][0], cube[0][0][1], cube[0][0][2]
        cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
        cube[4][0][0], cube[4][0][1], cube[4][0][2] = cube[2][2][2], cube[2][2][1], cube[2][2][0]
        cube[2][2][2], cube[2][2][1], cube[2][2][0] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
        cube[3][0][0], cube[3][0][1], cube[3][0][2] = tmp

init_cube = [[[] for _ in range(3)] for _ in range(6)]
# 큐브 초기상태 만들기
s = 'wrygbo'  # U F D L R B 순으로 채워넣음
for i in range(6):
    for j in range(3):
        for _ in range(3):
            init_cube[i][j].append(s[i])
# pprint.pprint(CUBE)

N = int(input())
for _ in range(N):
    n = int(input())
    order_list = input().split()
    cube = deepcopy(init_cube)

    while len(order_list) != 0:
        order = order_list.pop(0)
        if order[0] == 'L':
            left(order[1])
        elif order[0] == 'D':
            down(order[1])
        elif order[0] == 'U':
            up(order[1])
        elif order[0] == 'F':
            forward(order[1])
        elif order[0] == 'R':
            right(order[1])
        elif order[0] == 'B':
            backward(order[1])

    # 윗면 출력
    for i in range(3):
        print(''.join(cube[0][i]))
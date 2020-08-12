# 0. 인풋 정리
N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())    # 사과
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1
board[0][0] = 0

L = int(input())    # 명령
command = []
for _ in range(L):
    info = list(input().split())
    command.append([int(info[0]), info[1]])

    # 오  위  왼 아 (ccw)
di = [0, -1,  0, 1]
dj = [1,  0, -1, 0]


def eat():
    # 0. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    dir = bam[-1][2]
    ni = bam[-1][0] + di[dir]
    nj = bam[-1][1] + dj[dir]
    if 0 <= ni < N and 0 <= nj < N:
        # 벽 또는 자기자신의 몸과 부딪히면 게임이 끝
        for check_d in range(4):
            if [ni, nj, check_d] in bam:
                return False
        # 1-1. 만약 이동한 칸에 사과 O, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if board[ni][nj] == 1:
            bam.append([ni, nj, dir])
            board[ni][nj] = 0
        # 1-2. 만약 이동한 칸에 사과 X, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
        elif board[ni][nj] == 0:
            move()
        return True
    else:
        return False


def move():
    pre_dir = bam[-1][2]
    for n in range(len(bam)-1, -1, -1):     # 머리부터 이동
        bi, bj, bd = bam[n]
        bi, bj = bi+di[bd], bj+dj[bd]
        bam[n] = [bi, bj, pre_dir]

        pre_dir = bd


    #   i, j, d
bam = [[0, 0, 0]]
t = 0
while 1:
    if eat():
        t += 1
        if command:
            for c in command:
                if c[0] == t:
                    head_d = list(bam[-1])[2]
                    if c[1] == 'L':
                        head_d = (head_d + 1) % 4
                    elif c[1] == 'D':
                        head_d = (head_d - 1) % 4
                    bam[-1][2] = head_d
    else:
        t += 1
        break
print(t)
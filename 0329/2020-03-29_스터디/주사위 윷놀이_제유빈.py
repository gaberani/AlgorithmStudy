import sys

def dfs(idx, cnt):
    global max_cnt

    if idx == 10:
        if cnt > max_cnt:
            max_cnt = cnt
        return

    for i in range(4):
        x, y = start[i], start[i] # 이동 후, 이동전
        move = D[idx]   # 이동 거리

        # 파란 화살표 이동
        if x == 5:
            x = 22
            move -= 1
        elif x == 10:
            x = 25
            move -= 1
        elif x == 15:
            x = 27
            move -= 1

        # 한번에 이동
        if x + move <= 21:
            x += move
        # 한번에 이동 못하면
        else:
            # 한 칸씩 이동 => 뽑은 인덱스(I[x])를 새로운 인덱스 x 로 설정
            for _ in range(move):
                x = I[x]

        # 이미 다른 말이 있고 도착 지점이 아니면
        if c[x] and x != 21:
            continue         # 제외

        # dfs : x - 이동한 경우 y - 이동 안한 경우
        c[x], c[y], start[i] = 1, 0, x
        dfs(idx + 1, cnt + P[x])
        c[x], c[y], start[i] = 0, 1, y

D = list(map(int, sys.stdin.readline().split()))
# 다음 칸 인덱스 담은 리스트
I = [x for x in range(1, 22)]+[21, 23, 24, 30]+[26, 30]+[28, 29, 30]+[31, 32, 20]
# 게임 판 담은 리스트
P = [x for x in range(0, 41, 2)]+[0, 13, 16, 19]+[22, 24]+[28, 27, 26]+[25, 30, 35]

# 말의 위치 저장
start = [0]*4
# 게임 판 인덱스에 말이 있는지 표시 (visited)
c = [0]*33

max_cnt = 0
dfs(0, 0)
print(max_cnt)
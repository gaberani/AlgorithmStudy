# 2020-07-18 다시풀기
import sys

def dfs(idx, cnt):
    global max_cnt
    if idx == 10:
        if cnt > max_cnt: max_cnt = cnt
        return

    # 4개 말 이동
    for i in range(4):
        # 이동 전, 이동 후
        s, r = start[i], start[i]
        move = dice[idx]
        if r == 5:
            r = 22
            move -= 1
        elif r == 10:
            r = 25
            move -= 1
        elif r == 15:
            r = 27
            move -= 1

        # 빨간 화살표로 간 경우
        # 21번째 인덱스 이하인 경우
        # 21번째 인덱스의 값: 0
        if r + move <= 21:
            r += move
        # 아닌 경우
        else:
            # 다음 인덱스로 이동
            for _ in range(move):
                r = I[r]

        # 이미 다른 말이 있고 도착 지점도 아니면 이동 X
        if V[r] and r != 21:
            continue

        # 이동
        # s: 이동하기 전 지점, r: 이동 후 지점, start[i] : 말 인덱스 저장
        V[s], V[r], start[i] = 0, 1, r
        dfs(idx+1, cnt+P[r])
        V[s], V[r], start[i] = 1, 0, s

dice = list(map(int, sys.stdin.readline().split()))
# 다음 칸 시작 인덱스
# 20번 => 끝
I = list(range(1, 22)) + [21, 23, 24, 30] + [26, 30] + [28, 29, 30] + [31, 32, 20]
# 게임판 좌표
P = list(range(0, 41, 2)) + [0, 13, 16, 19] + [22, 24] + [28, 27, 26] + [25, 30, 35]

max_cnt = 0
# 말 4개 위치
start = [0]*4
V = [0]*33

dfs(0, 0)
print(max_cnt)






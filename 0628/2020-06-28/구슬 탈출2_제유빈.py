import sys
from collections import deque

# 구슬 이동
def move(r, c, dr, dc):
    cnt = 0
    # 벽이 있거나 구멍이 있으면 stop
    while P[r+dr][c+dc] != 1 and P[r][c] != 9:
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

# bfs 탐색
def game(red_r, red_c, blue_r, blue_c, cnt):
    global min_cnt, V
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    Q = deque()   # queue
    Q.append((red_r, red_c, blue_r, blue_c, cnt))
    V.append((red_r, red_c, blue_r, blue_c))
    while Q:
        red_r, red_c, blue_r, blue_c, cnt = Q.popleft()
        # 최소 cnt 넘어가거나 10 이상이면 중단
        if cnt >= 10 or cnt >= min_cnt:
            break
        # 기울이기
        for k in range(4):
            n_red_r, n_red_c, r_cnt = move(red_r, red_c, dr[k], dc[k])
            n_blue_r, n_blue_c, b_cnt = move(blue_r, blue_c, dr[k], dc[k])
            # 파란 공이 구멍에 빠졌을 때
            if P[n_blue_r][n_blue_c] == 9: continue
            # 빨간 공이 구멍에 빠졌을 때
            if P[n_red_r][n_red_c] == 9:
                cnt += 1
                if cnt < min_cnt:
                    min_cnt = cnt
                return
            # 공들이 같은 위치로 옮겨질 때
            if [n_red_r, n_red_c] == [n_blue_r, n_blue_c]:
                # 빨간 공 후퇴
                if r_cnt > b_cnt:
                    n_red_r -= dr[k]
                    n_red_c -= dc[k]
                # 파란 공 후퇴
                else:
                    n_blue_r -= dr[k]
                    n_blue_c -= dc[k]
            # 이전에 방문한 적이 없는 경우 이동
           if (n_red_r, n_red_c, n_blue_r, n_blue_c) not in V:
                Q.append((n_red_r, n_red_c, n_blue_r, n_blue_c, cnt+1))
                V.append((n_red_r, n_red_c, n_blue_r, n_blue_c))

N, M = map(int, sys.stdin.readline().split())
tmp = [list(sys.stdin.readline().strip()) for _ in range(N)]
P = [[0]*M for _ in range(N)]
V = []
min_cnt = 2**31-1
red_r, red_c, blue_r, blue_c = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if tmp[i][j] == '#': P[i][j] = 1
        elif tmp[i][j] == 'O': P[i][j] = 9
        else:
            P[i][j]=0
            if tmp[i][j] == 'R': red_r, red_c = i, j
            elif tmp[i][j] == 'B': blue_r, blue_c = i, j

game(red_r, red_c, blue_r, blue_c, 0)
if min_cnt == 2**31-1: min_cnt = -1
print(min_cnt)


# -------------------------------
#
# def game(red_r, red_c, blue_r, blue_c, cnt):
#     global min_cnt
#     dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
#     print(red_r, red_c, cnt)
#     if P[red_r][red_c] == 9 and cnt <= 10:
#         print('end')
#         print(red_r, red_c, cnt)
#         if cnt < min_cnt:
#             min_cnt = cnt
#     elif cnt > 10 or cnt >= min_cnt:
#         return
#     else:
#         for k in range(4):
#             n_red_r, n_red_c, r_cnt = move(red_r, red_c, dr[k], dc[k])
#             n_blue_r, n_blue_c, b_cnt = move(blue_r, blue_c, dr[k], dc[k])
#             if [n_red_r, n_red_c] == [red_r, red_c] and [n_blue_r, n_blue_c] == [blue_r, blue_c]:
#                 continue
#             if P[n_blue_r][n_blue_c] == 9: continue
#             if P[n_red_r][n_red_c] == 9:
#                 game(n_red_r, n_red_c, n_blue_r, n_blue_c, cnt+1)
#                 print('final')
#                 print(n_red_r, n_red_c, n_blue_r, n_blue_c, cnt)
#                 return
#             if [n_red_r, n_red_c] == [n_blue_r, n_blue_c]:
#                 if r_cnt > b_cnt:
#                     n_red_r -= dr[k]
#                     n_red_c -= dc[k]
#                 else:
#                     n_blue_r -= dr[k]
#                     n_blue_c -= dc[k]
#                 print('back')
#                 print(n_red_r, n_red_c, n_blue_r, n_blue_c)
#             if not V[n_red_r][n_red_c]:
#                 V[n_red_r][n_red_c] = 1
#                 print('recursion')
#                 print(n_red_r, n_red_c, n_blue_r, n_blue_c, cnt+1)
#                 game(n_red_r, n_red_c, n_blue_r, n_blue_c, cnt+1)
#                 V[n_red_r][n_red_c] = 0
#
#
# N, M = map(int, sys.stdin.readline().split())
# tmp = [list(sys.stdin.readline().strip()) for _ in range(N)]
# P = [[0]*M for _ in range(N)]
# V = []
# min_cnt = 2**31-1
# red_r, red_c, blue_r, blue_c = 0, 0, 0, 0
# for i in range(N):
#     for j in range(M):
#         if tmp[i][j] == '#': P[i][j] = 1
#         elif tmp[i][j] == '.': P[i][j] = 0
#         elif tmp[i][j] == 'O': P[i][j] = 9
#         elif tmp[i][j] == 'R': # 빨간색
#             P[i][j] = 0    # 2
#             red_r, red_c = i, j
#         elif tmp[i][j] == 'B': # 파란색
#             P[i][j] = 0    # 3
#             blue_r, blue_c = i, j
#
# game(red_r, red_c, blue_r, blue_c, 0)
#
# if min_cnt == 2**31-1: min_cnt = -1
#
# pprint.pprint(P)
# print(min_cnt)

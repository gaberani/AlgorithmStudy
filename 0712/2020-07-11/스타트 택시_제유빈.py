# # dfs
# import sys
#
# def min_dis(r, c, g_r, g_c, V, d):
#     global min_d, fuel, P
#     dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
#     if [r, c] == [g_r, g_c]:
#         # print(d, min_d)
#         if d < min_d:
#             min_d = d
#         return
#     elif d >= min(min_d, fuel): return
#     else:
#         for k in range(4):
#             nr, nc = r+dr[k], c+dc[k]
#             if 1 <= nr <= N and 1 <= nc <= N and not V[nr][nc] and not P[nr][nc]:
#                 V[nr][nc] = 1
#                 min_dis(nr, nc, g_r, g_c, V, d+1)
#                 V[nr][nc] = 0
#
#
# N, M, fuel = map(int, sys.stdin.readline().split())
# # 백준이 활동할 영역의 지도 - 0: 빈칸, 1: 벽
# P = [[1]*(N+2)]+[[1]+list(map(int, sys.stdin.readline().split()))+[1] for _ in range(N)]+[[1]*(N+2)]
# # 백준이 운전을 시작하는 칸의 행, 열
# R, C = map(int, sys.stdin.readline().split())
# # 승객의 출발지의 행, 열 + 목적지의 행, 열
# G = [list(map(int, sys.stdin.readline().split()))+[0] for _ in range(M)]
# r, c = R, C
# for _ in range(M):
#     # guests = deepcopy(G)
#     # print('--------')
#     # print(guests)
#     # print(G)
#     # print(fuel)
#     for guest in G:
#         min_d = N**2+1
#         s_r, s_c, f_r, f_c, d = guest
#         min_dis(r, c, s_r, s_c, [[1]*(N+2)]+[[1]+[0]*N+[1] for _ in range(N)]+[[1]*(N+2)], 0)
#         guest[-1] = min_d
#     # 거리 => 행 => 열 순서로 정렬
#     G.sort(key=lambda x: (x[-1], x[0], x[1]))
#     # guest = sorted(G, key=lambda x: (x[-1], x[0], x[1]))[0]
#     s_r, s_c, f_r, f_c, dist = G.pop(0)
#     # 모든 손님을 이동시킬 수 없을 때, 혹은 태우러 가지 못할 때 -1 출력하고 끝
#     if dist == N**2+1 or dist > fuel:
#         print(-1)
#         sys.exit()
#
#
#     fuel -= dist
#     min_d = N**2+1
#     min_dis(s_r, s_c, f_r, f_c, [[1]*(N+2)]+[[1]+[0]*N+[1] for _ in range(N)]+[[1]*(N+2)], 0)
#     if min_d == N**2+1 or min_d > fuel:
#         print(-1)
#         sys.exit()
#     fuel += min_d
#     # print(guests)
#
#     r, c = f_r, f_c
# print(fuel)
#
#
#
# # 모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양 출력
#
# # 이동 도중에 연료가 바닥나서 목적지로 이동할 수 없으면 -1
# # 모든 손님을 이동시킬 수 없을 때도 -1

# bfs
import sys
from collections import deque

def min_dis(r, c, g_r, g_c, V, d):
    global min_d, fuel, P
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    Q = deque()
    Q.append([r, c, 0])
    V[r][c] = 1
    while Q:
        r, c, d = Q.popleft()
        if [r, c] == [g_r, g_c]:
            if d < min_d:
                min_d = d
            return
        if d >= min(min_d, fuel):
            return
        for k in range(4):
            nr, nc = r+dr[k], c+dc[k]
            if 1 <= nr <= N and 1 <= nc <= N and not P[nr][nc] and not V[nr][nc]:
                V[nr][nc] = 1
                Q.append((nr, nc, d+1))


N, M, fuel = map(int, sys.stdin.readline().split())
# 백준이 활동할 영역의 지도 - 0: 빈칸, 1: 벽
P = [[1]*(N+2)]+[[1]+list(map(int, sys.stdin.readline().split()))+[1] for _ in range(N)]+[[1]*(N+2)]
# 백준이 운전을 시작하는 칸의 행, 열
R, C = map(int, sys.stdin.readline().split())
# 승객의 출발지의 행, 열 + 목적지의 행, 열
G = [list(map(int, sys.stdin.readline().split()))+[0] for _ in range(M)]
r, c = R, C
for _ in range(M):
    # guests = deepcopy(G)
    # print('--------')
    # print(guests)
    # print(G)
    # print(fuel)
    for guest in G:
        min_d = N**2+1
        s_r, s_c, f_r, f_c, d = guest
        min_dis(r, c, s_r, s_c, [[1]*(N+2)]+[[1]+[0]*N+[1] for _ in range(N)]+[[1]*(N+2)], 0)
        guest[-1] = min_d
    # 거리 => 행 => 열 순서로 정렬
    print(G)
    G.sort(key=lambda x: (x[-1], x[0], x[1]))
    print(G)
    # guest = sorted(G, key=lambda x: (x[-1], x[0], x[1]))[0]
    s_r, s_c, f_r, f_c, dist = G.pop(0)
    # 모든 손님을 이동시킬 수 없을 때, 혹은 태우러 가지 못할 때 -1 출력하고 끝
    if dist > fuel or dist == N**2+1:
        print(-1)
        sys.exit()


    fuel -= dist
    min_d = N**2+1
    min_dis(s_r, s_c, f_r, f_c, [[1]*(N+2)]+[[1]+[0]*N+[1] for _ in range(N)]+[[1]*(N+2)], 0)
    if min_d > fuel or min_d == N**2+1:
        print(-1)
        sys.exit()
    fuel += min_d
    # print(guests)
    r, c = f_r, f_c
print(fuel)



# 모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양 출력

# 이동 도중에 연료가 바닥나서 목적지로 이동할 수 없으면 -1
# 모든 손님을 이동시킬 수 없을 때도 -1



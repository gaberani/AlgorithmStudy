# 로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
# 한 칸 이동, 90도 회전에 걸리는 시간은 정확히 1초 입니다.
# (N, N) 위치까지 이동 시키기

from collections import deque
# 4방향 보내기 / 가로방향, 세로방향인 경우 확인해서 돌리기
def bfs(r1, r2, new_board):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    moves = []
    # 4방향
    for d in direction:
        if new_board[r1[0] + d[0]][r1[1] + d[1]] == 0 and new_board[r2[0] + d[0]][r2[1] + d[1]] == 0:
            moves.append({(r1[0] + d[0], r1[1] + d[1]), (r2[0] + d[0], r2[1] + d[1])})

    rotate = [1, -1]
    # 가로로 놓인 상태
    if r1[0] == r2[0]:
        for r in rotate:
            if new_board[r1[0] + r][r1[1]] == 0 and new_board[r2[0] + r][r2[1]] == 0:
                moves.append({(r1[0]+r, r1[1]), (r1[0], r1[1])})
                moves.append({(r2[0]+r, r2[1]), (r2[0], r2[1])})
    # 세로로 놓인 상태
    else:
        for r in rotate:
            if new_board[r1[0]][r1[1] + r] == 0 and new_board[r2[0]][r2[1] + r] == 0:
                moves.append({(r1[0], r1[1]), (r1[0], r1[1] + r)})
                moves.append({(r2[0], r2[1]), (r2[0], r2[1] + r)})
    return moves

def solution(board):
    L = len(board)
    # 테두리에 벽 추가
    new_board = [[1 for i in range(L+2)] for i in range(L+2)]
    # 좌표값 옮기기
    for i in range(L):
        for j in range(L):
            new_board[i+1][j+1] = board[i][j]

    que = deque()
    visit = []

    que.append([{(1, 1), (1, 2)}, 0])
    visit.append({(1, 1), (1, 2)})
    while len(que) != 0:
        temp = que.popleft()
        robot = list(temp[0])
        D = temp[1] + 1
        for move in bfs(robot[0], robot[1], new_board):
            if (L, L) in move:
                return D
            if not move in visit:
                que.append([move, D])
                visit.append(move)
    return 0



# # 일단 이동시킨다, 회전도 4가지 이므로 dfs로 되는 경우만 전부 보내면 되려나?
# import pprint
# def solution(board):
#     di = [0, -1,  0, 1]
#     dj = [1,  0, -1, 0]
#     ti = [1, -1, -1,  1]
#     tj = [1,  1, -1, -1]
#     #  반시계 ->  <- 시계
#     answer = 2**31-1
#     N = len(board)
#     # 미로 길 찾기
#     def dfs(i, j, rd, t):
#         nonlocal answer
#         if i == N-1 and j == N-1:
#             # 시간 비교, 갱신
#             if answer > t:
#                 answer = t
#         else:
#             # 이동 시키기(4방향)
#             for d in range(4):
#                 ni, nj, ni2, nj2 = i+di[d], j+dj[d], i+di[rd]+di[d], j+dj[rd]+dj[d]
#                 if 0 <= ni < N and 0 <= nj < N and 0 <= ni2 < N and 0 <= nj2 < N:
#                     if board[ni][nj] == 0 and board[ni2][nj2] == 0:
#                         board[ni][nj] = 2
#                         pprint.pprint(board)
#                         dfs(ni, nj, rd, t+1)
#                         board[ni][nj] = 0
#             # 회전 시키기(4가지) - 회전 시킨 뒤 rd를 바꿔서 준다.
#             rotate(i, j, rd, t)
#             pass
# 
#     # 본체 기준 시계
#     def rotate1(ri, rj, rd):
#         if rd != 3:
#             rd = (rd + 1) % 4
#             ni, nj = ri + di[rd], rj + dj[rd]
#             board[ri][rj] = 2; board[ni][nj] = 2
# 
#             board[ri][rj] = 0; board[ni][nj] = 0
#             rotate1(ri, rj, rd)
# 
#     # 따라오는애 기준
#     def rotate2(ri, rj, rd):
#         if rd != 3:
#             ni, nj = ri + di[rd], rj + dj[rd]  # 따라오는애 위치찾기
#             nrd = (rd + 1) % 4
#             new_ri, new_rj = ni - di[nrd], nj - dj[nrd]  # 본체의 바뀐 위치
#             if board[ni + ti[rd]][nj + tj[rd]] == 0:
#                 board[ni][nj] = 2; board[new_ri][new_rj] = 2
# 
#                 board[ni][nj] = 0; board[new_ri][new_rj] = 0
#             rotate2(new_ri, new_rj, nrd)
#     # 시계, 반시계 회전 시키는 함수
#     def rotate(i, j, rd, t):
#         ni2, nj2 = i+di[rd], j+dj[rd]
#         # 각 방향에 맞는 대각선 좌표가 0인지 확인하고 회전
#         # 좌표1을 기준으로 시계
#         # ni, nj =
#         if board[ni2][nj2] == 0:
#             dfs(i, j, (rd+1)%4, t+1)
#         # 좌표1을 기준으로 반시계
#         if board[ni2][nj2] == 0:
#             dfs(i, j, (rd-1)%4, t+1)
#         # 좌표2를 기준으로 시계
#         if board[i][j] == 0:
#             dfs(ni2-di[(rd-1)%4], nj2-dj[(rd-1)%4], (rd-1)%4, t+1)
#         # 좌표2를 기준으로 반시계
#         if board[i][j] == 0:
#             dfs(ni2-di[(rd+1)%4], nj2-dj[(rd+1)%4], (rd+1)%4, t+1)
#     ri, rj, rd = 0, 0, 0
#     board[ri][rj] = 2
#     # board[ri][rj], board[ri + di[rd]][dj[rd]] = 2, 2
#     dfs(ri, rj, rd, 0)
#     # pprint.pprint(board)
#     return answer
# 
# 
# def solution2(board):
#     di = [0, -1,  0, 1]
#     dj = [1,  0, -1, 0]
#     ti = [1, -1, -1,  1]
#     tj = [1,  1, -1, -1]
#     #  반시계 ->  <- 시계
#     answer = 2**31-1
#     N = len(board)
#     # 미로 길 찾기
#     def dfs(r1, r2, t):
#         nonlocal answer
#         if (r1[0] == N-1 and r1[1] == N-1) or (r2[0] == N-1 and r2[1] == N-1):
#             # 시간 비교, 갱신
#             if answer > t:
#                 answer = t
#         else:
#             # 이동 시키기(4방향)
#             for d in range(4):
#                 ri1, rj1, ri2, rj2 = r1[0]+di[d], r1[1]+dj[d], r2[0]+di[d], r2[1]+dj[d]
#                 if 0 <= ri1 < N and 0 <= rj1 < N and 0 <= ri2 < N and 0 <= rj2 < N:
#                     if board[ri1][rj1] != 1 and board[ri2][rj2] != 1: # 벽만 아니면 갈 수 있음
#                         board[ri1][rj1], board[ri2][rj2] = 2, 2
#                         pprint.pprint(board)
#                         dfs(r1, r2, t+1)
#                         board[ri1][rj1], board[ri2][rj2] = 0, 0
# 
#             # 회전 시키기(4가지) - 회전 시킨 뒤 rd를 바꿔서 준다.
#             rotate(r1, r2, t, 0)
# 
#             # for t in range(4):
#             #     nt =
#             #     ri1, rj1, mi2, mj2 = r1[0]+ti[t], r1[1]+tj[t], r2[0], r2[1]  # 부속 좌표
#             #
# 
# 
#             # 시계
#             pass
# 
#     def rotate(r1, r2, t, td):
#         if td == 0: # 가로 상태
#         for d in range(4):
#             ri1, rj1, ri2, rj2 = r1[0]+ti[d], r1[1]+tj[d], r2[0], r2[1]  # 부속 좌표
#             # 영역안에 있는지 확인
#             if 0 <= ri1 < N and 0 <= rj1 < N:
#                 # 대각선에 0인지 확인
#         else: # 세로 상태
# 
#     # board[ri][rj] = 2
#     # board[ri][rj], board[ri + di[rd]][dj[rd]] = 2, 2
#     dfs([0, 0], [0, 1], 0)
# 
# 
# 
# # answer = 7
# print(solution2([[0, 0, 0, 1, 1],
#                 [0, 0, 0, 1, 0],
#                 [0, 1, 0, 1, 1],
#                 [1, 1, 0, 0, 1],
#                 [0, 0, 0, 0, 0]]))
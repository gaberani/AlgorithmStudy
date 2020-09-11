def solution():
    answer = 0
    return answer

# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))


# di = [0, 1,  0, -1]
# dj = [1, 0, -1, 0]
# import pprint
# def dfs(si, sj, cost, board, N, visit, pre):
#     global answer
#     # 도착 했으면
#     if si == N-1 and sj == N-1:
#         if answer > cost:
#             answer = cost
#             pprint.pprint(visit)
#             print(cost)
#     # 아직 도착 안했으면
#     elif answer < cost:
#         return
#     else:
#         for d in range(4):
#             ni, nj = si+di[d], sj+dj[d]
#             if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 0 and visit[ni][nj] == 0:
#                 # 직선 도로
#                 if not cost == 0:
#                     if pre%2 == d%2:
#                         visit[ni][nj] = 1
#                         dfs(ni, nj, cost+100, board, N, visit, d)
#                         visit[ni][nj] = 0
#                     # 곡선 도로
#                     else:
#                         visit[ni][nj] = 1
#                         dfs(ni, nj, cost+600, board, N, visit, d)
#                         visit[ni][nj] = 0
#                 else:
#                     visit[ni][nj] = 1
#                     dfs(ni, nj, cost + 100, board, N, visit, d)
#                     visit[ni][nj] = 0
#
# answer = 2**31-1
# def solution(board):
#     N = len(board)
#     visit = [[0]*N for _ in range(N)]
#     visit[0][0] = 1
#     pprint.pprint(board)
#     print('-------------')
#     dfs(0, 0, 0, board, N, visit, -1)
#     return answer
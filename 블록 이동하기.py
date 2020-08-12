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
    # 큐 설정
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
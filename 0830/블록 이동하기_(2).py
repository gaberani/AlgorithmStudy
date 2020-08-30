from collections import deque

# 해당 위치에서 4방향 보내기 / 가로방향 or 세로방향인지 체크해서 가능한 경우 전부 담아서 리턴
def bfs(r1, r2, new_board):
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    cases = []

    # 1. 4방향 이동
    for d in dir:
        if new_board[r1[0] + d[0]][r1[1] + d[1]] == 0 and new_board[r2[0] + d[0]][r2[1] + d[1]] == 0:
            cases.append({(r1[0] + d[0], r1[1] + d[1]), (r2[0] + d[0], r2[1] + d[1])})

    rotate = [1, -1]
    # 2. 가로회전 시키는 경우
    if r1[0] == r2[0]:
        for r in rotate:
            if new_board[r1[0] + r][r1[1]] == 0 and new_board[r2[0] + r][r2[1]] == 0:
                cases.append({(r1[0]+r, r1[1]), (r1[0], r1[1])})
                cases.append({(r2[0]+r, r2[1]), (r2[0], r2[1])})

    # 3. 세로회전 시키는 경우
    else:
        for r in rotate:
            if new_board[r1[0]][r1[1] + r] == 0 and new_board[r2[0]][r2[1] + r] == 0:
                cases.append({(r1[0], r1[1]), (r1[0], r1[1] + r)})
                cases.append({(r2[0], r2[1]), (r2[0], r2[1] + r)})
    return cases

def solution(board):
    L = len(board)
    # 전부 1로 칠하면서 테두리에 벽 추가
    new_board = [[1 for i in range(L+2)] for i in range(L+2)]
    # 좌표값 옮기기
    for i in range(L):
        for j in range(L):
            new_board[i+1][j+1] = board[i][j]

    # 큐와 방문 여부 체크리스트
    q = deque()
    visit = []
    q.append([{(1, 1), (1, 2)}, 0])
    visit.append({(1, 1), (1, 2)})

    while q:
        temp = q.popleft()
        robot = list(temp[0])
        D = temp[1] + 1
        for m in bfs(robot[0], robot[1], new_board):
            # 도착하면 최소 시간으로 바로 리턴
            if (L, L) in m:
                return D
            #
            if not m in visit:
                q.append([m, D])
                visit.append(m)

    # 도착 못할 경우 0 리턴
    return 0
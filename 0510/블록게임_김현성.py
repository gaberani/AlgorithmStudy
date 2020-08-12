# 25 / 100

import pprint
di = [1, 0, -1,  0]
dj = [0, 1,  0, -1]

ok_block = [[[0, 0], [1, 0], [1, 1], [1, 2]],
            [[0, 1], [1, 1], [2, 0], [2, 1]],
            [[0, 0], [1, 0], [2, 0], [2, 1]],
            [[0, 2], [1, 0], [1, 1], [1, 2]],
            [[0, 1], [1, 0], [1, 1], [1, 2]]
            ]

answer = 0
def dfs(si, sj, v, block, board, visit):
    global answer
    if len(block) == 4:
        block = sorted(block)
        # x, y 좌표 최솟값 찾기
        min_x, min_y = N, N
        for b in block:
            if min_x > b[0]:
                min_x = b[0]
            if min_y > b[1]:
                min_y = b[1]
        # ok_block과 비교하기 위해 최솟값 빼줌
        for b in range(4):
            block[b][0] -= min_x
            block[b][1] -= min_y
        print(v, sorted(block))
        # ok_block과 비교
        for ok in range(5):
            if sorted(block) == ok_block[ok]:   # 만들 수 있는 블록이면
                # 위에 뭔가 있는 지 확인 (check 함수)
                if check(sorted(block), board, min_x, min_y, v):
                    # 위에 아무것도 없으면 board에서 지움
                    for b in range(4):
                        board[block[b][0]+min_x][block[b][1]+min_y] = 0
                    answer += 1
    else:
        # 같은 값 block 좌표 찾기
        for d in range(4):
            ni, nj = si+di[d], sj+dj[d]
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == v and [ni, nj] not in block:
                block.append([ni, nj])
                visit[ni][nj] = 1
                dfs(ni, nj, v, block, board, visit)

def check(B, board, min_x, min_y, v):
    # 기존 좌표로 되돌리기
    for b in range(4):
        ni = B[b][0] + min_x
        nj = B[b][1] + min_y
        # 위에 뭔가 없는지 확인
        while board[ni][nj] == v or board[ni][nj] == 0:
            ni -= 1
            if ni == -1: # 탈출 조건
                break
        if ni != -1:    # while 문 끝났는데 -1 아니면 False
            return False
    return True # for문 전부 돌면 True

def solution(board):
    global N
    N = len(board)
    visit = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and visit[i][j] == 0:
                dfs(i, j, board[i][j], [[i, j]], board, visit)
                visit[i][j] = 0
        for j in range(N-1, -1, -1):
            if board[i][j] != 0 and visit[i][j] == 0:
                dfs(i, j, board[i][j], [[i, j]], board, visit)
    # pprint.pprint(board)
    return answer

print(solution([[0,8,0,0,7,0,0,0,0,0],
                [0,8,7,7,7,0,0,0,0,0],
                [0,8,8,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,4,0,0,0],
                [0,0,0,0,0,0,4,0,0,0],
                [0,0,0,0,0,0,4,0,0,0],
                [0,0,0,2,0,0,0,0,5,5],
                [1,2,2,2,9,0,0,0,0,5],
                [1,1,1,9,9,9,0,0,0,5]]))
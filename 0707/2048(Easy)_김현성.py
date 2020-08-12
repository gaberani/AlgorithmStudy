# 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록
from copy import deepcopy
# 0. 인풋 정리
N = int(input())    # 보드의 크기
board = [[] for _ in range(N)]
for _ in range(N):
    board[_] = list(map(int, input().split()))

#     왼  위   오 아
di = [ 0, -1,  0, 1]
dj = [-1,  0,  1, 0]

def dfs(d, cnt, board):
    global MaxValue
    # 5번 다돌렸으면
    game = deepcopy(board)
    if cnt == 6:
        # 최대값 갱신
        for i in range(N):
            for j in range(N):
                if MaxValue < game[i][j]:
                    MaxValue = game[i][j]
    # 5번 될때까지 돌리기
    else:
        if d == 0:      # 왼쪽 밀기
            for i in range(N):
                for j in range(N):
                    if game[i][j]:  # 값이 0이 아니면
                        for nj in range(j+1, N):
                            if game[i][nj] == game[i][j]:
                                game[i][nj] = 0
                                game[i][j] += game[i][j]
                                break
                            elif game[i][nj] == 0:
                                continue
                            else:
                                break
                        for pj in range(j-1, -1, -1):
                            if game[i][pj]:
                                game[i][pj+1], game[i][j] = game[i][j], game[i][pj+1]
                                break
                            if game[i][pj] == 0 and pj == 0:
                                game[i][pj], game[i][j] = game[i][j], game[i][pj]
        elif d == 1:    # 위쪽 밀기
            for j in range(N):
                for i in range(N):
                    if game[i][j]:  # 값이 0이 아니면 시작
                        # 0 아닌 것 찾기
                        for ni in range(i+1, N):
                            if game[ni][j] == game[i][j]:
                                game[ni][j] = 0
                                game[i][j] += game[i][j]
                                break
                            elif game[ni][j] == 0:
                                continue
                            else:
                                break
                        for pi in range(i-1, -1, -1):
                            if game[pi][j]:
                                game[pi+1][j], game[i][j] = game[i][j], game[pi+1][j]
                                break
                            elif game[pi][j] == 0 and pi == 0:
                                game[pi][j], game[i][j] = game[i][j], game[pi][j]
        elif d == 2:    # 오른쪽 밀기
            for i in range(N):
                for j in range(N-1, -1, -1):
                    if game[i][j]:  # 값이 0이 아니면
                        for nj in range(j-1, -1, -1):
                            if game[i][nj] == game[i][j]:
                                game[i][nj] = 0
                                game[i][j] += game[i][j]
                                break
                            elif game[i][nj] == 0:
                                continue
                            else:
                                break
                        for pj in range(j+1, N):
                            if game[i][pj]:
                                game[i][j], game[i][pj-1] = game[i][pj-1], game[i][j]
                                break
                            elif game[i][pj] == 0 and pj == N-1:
                                game[i][pj], game[i][j] = game[i][j], game[i][pj]
        elif d == 3:    # 아래쪽 밀기
            for j in range(N):
                for i in range(N-1, -1, -1):
                    if game[i][j]:  # 값이 0이 아니면
                        for ni in range(i-1, -1, -1):
                            if game[ni][j] == game[i][j]:
                                game[ni][j] = 0
                                game[i][j] += game[i][j]
                                break
                            elif game[ni][j] == 0:
                                continue
                            else:
                                break
                        for pi in range(i+1, N):
                            if game[pi][j]:
                                game[pi-1][j], game[i][j] = game[i][j], game[pi-1][j]
                                break
                            elif game[pi][j] == 0 and pi == N-1:
                                game[pi][j], game[i][j] = game[i][j], game[pi][j]
        for nd in range(4):
            dfs(nd, cnt+1, game)
MaxValue = 0

# 1. dfs로 각 방향 5번
for i in range(4):
    dfs(i, 1, board)
print(MaxValue)
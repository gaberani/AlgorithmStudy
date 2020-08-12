from _collections import deque

def solution(board):
    N = len(board)
    P = [[1] * (N+2)] + [[1] + board[i] + [1] for i in range(N)] + [[1] * (N+2)]
    Q, V = deque(), []
    Q.append([(1, 1), (1, 2)])  # queue
    V.append([(1, 1), (1, 2)])  # visited
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0] # 오 왼 위 아
    time = 0

    # 회전
    def rotate(robot, i, dir):  # dir 0 : 가로 , 1 : 세로
        # 가로 모양으로 돌아오고, 위 아래 회전 요청
        if not dir:
            for k in range(2):
                n1 = robot[k]  # 점 그대로
                n2 = (robot[k][0] + dr[i], robot[k][1])  # 새로운 점
                new = sorted([n1, n2])
                if new not in V:
                    Q.append(new)
                    V.append(new)
        else:
            for k in range(2):
                n1 = robot[k]  # 점 그대로
                n2 = (robot[k][0], robot[k][1] + dc[i])  # 새로운 점
                new = sorted([n1, n2])
                if new not in V:
                    Q.append(new)
                    V.append(new)
    while Q:
        for _ in range(len(Q)):
            robot = Q.popleft()
            if robot == [(N-1, N), (N, N)] or robot == [(N, N-1), (N, N)]:
                return time
            for i in range(4):
                new, flag = [0, 0], True
                for j in range(2):
                    nr = robot[j][0] + dr[i]
                    nc = robot[j][1] + dc[i]
                    if 0 < nr <= N and 0 < nc <= N and not P[nr][nc]:
                        new[j] = (nr, nc)
                    else:
                        flag = False
                        break
                if flag:
                    # 새로운 점 추가
                    new = sorted(new)
                    if new not in V:
                        Q.append(new)
                        V.append(new)
                    # 회전
                    # 가로 모양이면
                    if robot[0][0] == robot[1][0]:
                        # 위 아래
                        if i > 1:
                            rotate(robot, i, 0)
                    # 세로 모양이면
                    elif robot[0][1] == robot[1][1]:
                        # 오 왼 이동
                        if i <= 1:
                            rotate(robot, i, 1)
        time += 1



print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def solution(board):
    answer = 0
    # 지도 길이
    N = len(board)
    # 주어진 board를 1로 둘러싸기
    for i in range(N):
        board[i] = [1]+board[i]+[1]
    board = [[1]*(N+2)]+board+[[1]*(N+2)]
    # 로봇 좌표 (가로 방향일 땐 [왼, 오], 세로 방향일 땐 [위, 아래])
    robot = [[1, 1], [1, 2]]
    # 로봇이 지나온 경로 표시
    v = [robot]
    q = [robot+[0]+[v]]
    while q:
        # 로봇 좌표, 걸린 시간, 경로
        r1, r2, cnt, v = q.pop(0)
        # 로봇이 도착하면
        if r2==[N, N]:
            answer = cnt
            break
            
        for d in range(4):
            # 로봇이 회전하지 않고 상, 하, 좌, 우로 이동할 때
            # n1, n2 = 새로운 로봇 좌표
            n1, n2 = [r1[0]+di[d], r1[1]+dj[d]], [r2[0]+di[d], r2[1]+dj[d]]
            # 새로운 좌표가 지도 안에 있고, 벽이 아닐 때
            if 1<=n1[0]<=N and 1<=n1[1]<=N and 1<=n2[0]<=N and 1<=n2[1]<=N and not board[n1[0]][n1[1]] and not board[n2[0]][n2[1]]:
                # 새로운 좌표가 이미 지나온 경로에 있는지 확인
                if [n1, n2] not in v:
                    v.append([n1, n2])
                    q.append([n1, n2, cnt+1, v])
            
            # 로봇이 세로방향일 때
            if d==0  and r1[1]==r2[1]:
                # r1을 중심으로 반시계 90도 회전
                n1, n2 = r1, [r1[0]+di[d], r1[1]+dj[d]]
                # 회전할 때는 회전반경에 벽이 없는지 추가로 검사해야 한다
                if 1<=n2[0]<=N and 1<=n2[1]<=N and not board[n2[0]+1][n2[1]] and not board[n2[0]][n2[1]]:
                    if [n1, n2] not in v:
                        v.append([n1, n2])
                        q.append([n1, n2, cnt+1, v])
                # r2을 중심으로 시계 90도 회전
                n1, n2 = r2, [r2[0]+di[d], r2[1]+dj[d]]
                if 1<=n2[0]<=N and 1<=n2[1]<=N and not board[n2[0]-1][n2[1]] and not board[n2[0]][n2[1]]:
                    if [n1, n2] not in v:
                        v.append([n1, n2])
                        q.append([n1, n2, cnt+1, v])
            # 로봇이 세로 방향일 때
            elif d==1  and r1[1]==r2[1]:
                # r1을 중심으로 시계 90도 회전
                n1, n2 = [r1[0]+di[d], r1[1]+dj[d]], r1
                if 1<=n1[0]<=N and 1<=n1[1]<=N and not board[n1[0]+1][n1[1]] and not board[n1[0]][n1[1]]:
                    if [n1, n2] not in v:
                        v.append([n1, n2])
                        q.append([n1, n2, cnt+1, v])
                # r2을 중심으로 반시계 90도 회전
                n1, n2 = [r2[0]+di[d], r2[1]+dj[d]], r2
                if 1<=n1[0]<=N and 1<=n1[1]<=N and not board[n1[0]-1][n1[1]] and not board[n1[0]][n1[1]]:
                    if [n1, n2] not in v:
                        v.append([n1, n2])
                        q.append([n1, n2, cnt+1, v])
            # 로봇이 가로 방향일 때
            elif d==2  and r1[0]==r2[0]:
                # r1을 중심으로 시계 90도 회전
                n1, n2 = r1, [r1[0]+di[d], r1[1]+dj[d]]
                if 1<=n2[0]<=N and 1<=n2[1]<=N and not board[n2[0]][n2[1]+1] and not board[n2[0]][n2[1]]:
                    if [n1, n2] not in v:
                        v.append([n1, n2])
                        q.append([n1, n2, cnt+1, v])
                # r2을 중심으로 반시계 90도 회전
                n1, n2 = r2, [r2[0]+di[d], r2[1]+dj[d]]
                if 1<=n2[0]<=N and 1<=n2[1]<=N and not board[n2[0]][n2[1]-1] and not board[n2[0]][n2[1]]:
                    if [n1, n2] not in v:
                        v.append([n1, n2])
                        q.append([n1, n2, cnt+1, v])
            # 로봇이 가로 방향일 때
            elif d==3  and r1[0]==r2[0]:
                # r1을 중심으로 반시계 90도 회전
                n1, n2 = [r1[0]+di[d], r1[1]+dj[d]], r1
                if 1<=n1[0]<=N and 1<=n1[1]<=N and not board[n1[0]][n1[1]+1] and not board[n1[0]][n1[1]]:
                    if [n1, n2] not in v:
                        v.append([n1, n2])
                        q.append([n1, n2, cnt+1, v])
                # r2을 중심으로 시계 90도 회전
                n1, n2 = [r2[0]+di[d], r2[1]+dj[d]], r2
                if 1<=n1[0]<=N and 1<=n1[1]<=N and not board[n1[0]][n1[1]-1] and not board[n1[0]][n1[1]]:
                    if [n1, n2] not in v:
                        v.append([n1, n2])
                        q.append([n1, n2, cnt+1, v])

    return answer

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# result = 7

print(solution(board))
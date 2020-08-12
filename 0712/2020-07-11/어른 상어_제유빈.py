import sys

N, M, k = map(int, sys.stdin.readline().split())
# 격자
P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 각 상어의 방향
dirs = [0] + list(map(int, sys.stdin.readline().split()))
# 우선순위 => 위 아래 왼쪽 오른쪽, 1, 2, 3, 4: 위 아래 왼 오
# i: 상어 번호, j: 상어가 바라보는 방향, val: 우선순위 방향 순서
priority = {i: {j: list(map(int, sys.stdin.readline().split())) for j in range(1, 5)} for i in range(1, M+1)}
dr, dc = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]

# bfs
# 상어 좌표 저장
shark = [0]*(M+1)
for i in range(N):
    for j in range(N):
        if P[i][j]:
            shark[P[i][j]] = [i, j, dirs[P[i][j]]]
            P[i][j] = [P[i][j], k]

for time in range(1, 1002):
    # 1000초 넘으면 -1 출력
    if time > 1000:
        print(-1)
        break

    # 상어 이동 내용 저장
    V = [[0]*N for _ in range(N)]

    # 상어 이동
    for i in range(1, M+1):
        # 상어 정보 없으면 지나감
        if not shark[i]:
            continue
        # 각 상어 정보에 대해
        r, c, d = shark[i]  # 행, 열, 방향

        # 1. 인접한 칸 중 아무 냄새가 없는 칸의 방향
        for j in range(4):
            new_d = priority[i][d][j]
            nr, nc = r+dr[new_d], c+dc[new_d]
            if 0 <= nr < N and 0 <= nc < N and not P[nr][nc]:
                break

        # 2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향
        else:
            for j in range(4):
                new_d = priority[i][d][j]
                nr, nc = r+dr[new_d], c+dc[new_d]
                # 자신의 정보가 있는 칸이면 break
                if 0 <= nr < N and 0 <= nc < N and P[nr][nc][0] == i+1:
                    break

        # 움직이려는 점에 상어 정보가 있으면
        if V[nr][nc]:
            # 저장된 값이 현재 상어 번호보다 크거나 같으면
            if V[nr][nc] >= i:
                # 이전 상어 정보가 없어진다.
                shark[V[nr][nc]] = 0
            # 아닌 경우
            else:
                # 현재 상어 정보 없어짐
                shark[i] = 0
        # 이전에 저장된 상어 정보가 없는 경우
        else:
            # 상어 정보 저장
            V[nr][nc] = i
            shark[i] = [nr, nc, new_d]

    # 냄새 숫자 하나씩 줄이기
    for row in range(N):
        for col in range(N):
            if P[row][col]:
                P[row][col][1] -= 1
                # 아예 값이 없어지는 경우
                if not P[row][col][1]:
                    P[row][col] = 0

    # 이동된 점에 상어 정보 저장
    for i in range(1, M+1):
        if shark[i]:
            r, c = shark[i][:-1]
            # 이동된 점에 정보 저장
            P[r][c] = [i+1, k]끝

    # 상어가 한 마리 남았을 경우 시간 출력 후
    if shark.count(0) == M-1:
        print(time)
        break

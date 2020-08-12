# 2020-07-17 다시풀기
import sys
import pprint
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 방향 : 0 - 북, 1 - 동, 2 - 남, 3 - 서
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
clean = 1
# 1. 현재 위치 청소
while 1:
    print(r, c, d)
    pprint.pprint(P)
    P[r][c] = 2
    new_d = d
    # 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색 진행
    for _ in range(4):
        new_d = (new_d-1)%4
        nr, nc = r+dr[new_d], c+dc[new_d]
        if 0 <= nr < N and 0 <= nc < M:
            # 2-1. 왼쪽 방향에서 아직 청소하지 않은 공간이 존재한다면
            if not P[nr][nc]:
                # 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행
                P[nr][nc] = 2
                clean += 1
                r, c, d = nr, nc, new_d
                break
            # 2-2. 왼쪽 방향에 청소할 공간이 없다면
            # 그 방향으로 회전하고 2번으로 돌아감
    # 2-3. 네 방향 모두 청소가 되어있거나 벽인 경우
    else:
        nr, nc = r-dr[d], c-dc[d]
        if 0 <= nr < N and 0 <= nc < M:
            # 후진할 수 있는 경우
            if P[nr][nc] != 1:
                # 바라보는 방향을 유지한 채로 한 칸을 후진하고 2번으로 돌아감
                r, c = nr, nc
            # 후진할 수 없는 경우
            else:
                # 청소기가 청소하는 칸의 개수 출력
                print(clean)
                # 작동을 멈춘다
                sys.exit()


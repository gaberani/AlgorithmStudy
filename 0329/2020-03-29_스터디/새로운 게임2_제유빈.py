import sys

def game():
    for n in range(1, K+1):    # n 번째, position, dir 인덱스 번호 같음
        r, c = position[n]
        d = dir[n]
        # 다음 점과 방향을 찾는다.
        tr, tc = r, c
        # 움직일 수 있으면
        if check(r+dr[d], c+dc[d]):
            tr, tc = r + dr[d], c + dc[d]
        # 못움직이면
        else:
            # 방향 반대로 이동
            if d%2:
                d -= 1
            else:
                d += 1
            # 반대 방향으로 움직일 수 있으면 이동
            if check(r+dr[d], c+dc[d]):
                tr, tc = r+dr[d], c+dc[d]
        dir[n] = d    # 방향 저장

        # 같은 지점이면 패스 (이동 못하는 경우)
        if [r, c] == [tr, tc]:
            continue

        idx = V[r][c].index(n)   # 해당 말이 몇 번째에 쌓여있는지 인덱스 확인
        move(r, c, tr, tc, idx)  # 움직인다!
        temp = V[r][c][idx:]     # 움직일 말들
        V[r][c] = V[r][c][:idx]  # 움직이지 않을 말들
        if P[tr][tc] == 0:       # 흰 배경이면 / 그대로 움직임
            V[tr][tc] += temp[:] # 움직일 말들 뒤에 추가
        elif P[tr][tc] == 1:     # 빨간 배경이면 / 순서 바꿔서 움직임
            V[tr][tc] += temp[::-1] # 움직일 말들 순서 바꿔서 추가
        if len(V[tr][tc]) >= 4:     # 말이 4개 이상이면 게임 종료
            return 1
    return 0

# position 이동
def move(r, c, tr, tc, idx):
    for n in V[r][c][idx:]:    # n번째 이후에 쌓여 있는 말들의
        position[n] = [tr, tc] # 위치를 바꿔준다

# 이동 못하는 경우 확인(파란색 말(2), 또는 범위 밖으로 나갈 때)
def check(r, c):
    if not 0 <= r < N or not 0 <= c < N:
        return 0
    if P[r][c] == 2:
        return 0
    return 1

N, K = map(int, sys.stdin.readline().split())
P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
C = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
V = [[[] for _ in range(N)] for _ in range(N)]  # 체스 번호 저장
position, dir = [0], [0]
dr = [0, 0, -1, 1]  # 오 왼 위 아래
dc = [1, -1, 0, 0]

for i in range(K):
    x, y, d = C[i]          # 행, 열, 방향
    x, y, d = x-1, y-1, d-1
    V[x][y].append(i+1)     # 현재 체스판에 있는 말의 번호를 저장한다.
    position.append([x, y]) # 말의 위치를 저장
    dir.append(d)           # 말의 방향 저장

turn = 0 # 게임이 종료되는 턴
while 1:
    turn += 1
    if turn > 1000:    # 턴이 1000보다 크거나 종료되지 않으면
        print(-1)      # -1 출력
        break
    if game():         # 게임이 종료되면(말이 4개 이상 쌓이면) 1 반환
        print(turn)
        break
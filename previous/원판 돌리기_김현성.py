di = [1, -1, 0,  0]
dj = [0,  0, 1, -1]

# 회전 시키는 함수
def turn(x, d, k):
    for n in range(1, N+1): # 원판이
        if not n%X:         # X로 나누어 떨어지면
            if not d:   # 시계
                for _ in range(k):
                    temp = won[n-1][-1]
                    won[n-1] = [temp] + won[n-1][:M-1]
            else:   # 반시계
                for _ in range(k):
                    temp = won[n-1][0]
                    won[n-1] = won[n-1][1:M] + [temp]
    return near()

# 인접한 수 확인하고 그에 대한 처리 함수
def near():
    cnt = 0     # 하나라도 인접하지 않은지 체크
    cntN = 0    # 숫자 남은 개수
    totN = 0    # 숫자의 총합
    for i in range(N):
        for j in range(M):
            flag = 0        # 각 숫자마다 flag 갱신
            if won[i][j] != 0:  # 0이 아니라면
                s = []
                v = [[0] * M for _ in range(N)]
                s.append((i, j))
                v[i][j] = 1
                while len(s) != 0:
                    x, y = s.pop()
                    for k in range(4):  # 4방향 체크
                        nx, ny = x + di[k], (y + dj[k] + M) % M     # i는 원판 크기 위아래, j는 양 옆 체크
                        if 0 <= nx <= N-1 and 0 <= ny <= M-1:   # 인덱스 범위 확인
                            if won[x][y] == won[nx][ny] and v[nx][ny] == 0:        # 인접한 수 같고 방문하지 않은 곳이면
                                flag = 1            # 1개라도 중복하는지 체크
                                v[nx][ny] = 1
                                s.append((nx, ny))    # stack ++
                if not flag :    # 1개도 중복하지 않으면(& 0이 아님)
                    cntN += 1
                    totN += won[i][j]
                else:           # 1개라도 중복하면
                    cnt = 1
                    for ei in range(N):
                        for ej in range(M):
                            if v[ei][ej]:
                                won[ei][ej] = 0

    # 돌린 뒤 인접하면서 같은 수가 하나도 없다면
    if cnt == 0 and cntN != 0:
        mid = totN/cntN     # 원판에 적힌 수의 평균 구하고
        for i in range(N):
            for j in range(M):
                # 평균보다 큰 수에서 1빼고, 작은 수엔 1더함
                if won[i][j] != 0:
                    if won[i][j] > mid:
                        won[i][j] -= 1
                        totN -= 1
                    elif won[i][j] < mid:
                        won[i][j] += 1
                        totN += 1
    return totN

# N: 원판 크기, M: 정수의 개수, T: 회전 횟수
N, M ,T = map(int, input().split())
won = [list(map(int, input().split())) for _ in range(N)]
# X: x의 배수인 원판 / D: 0은 시계, 1은 반시계 / K: 몇 칸 돌릴지
for t in range(T):
    X, D, K = map(int, input().split())
    result = turn(X, D, K)
print(result)
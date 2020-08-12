def f(n, k, ni, nj):
    global ba, V, toth, base
    if n == k:
        sumba = sum(ba)
        totba = 0
        for nba in ba:
            totba += nba**2
        if sumba <= C and base < totba:
            base = totba
            newh[ni][nj] = totba
    else:
        for i in range(n, M):
            if not V[i]:
                V[i] = 1
                ba[n] = A[i]
                f(n+1, k, ni, nj)
                V[i] = 0

def ggool(a, ni, nj):
    global ba, V, toth, base
    suma = sum(a)
    tota = 0
    base = 0
    for na in a:
        tota += na**2
    if suma <= C:
        newh[ni][nj] = tota
    else:
        for m in range(1, M):   # 부분 집합 구하기
            ba = [0]*m  # 만들 부분집합 크기
            V = [0]*M   # 방문 표시
            f(0, m, ni, nj)

T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    # N: 벌통의 크기, M: 선택할 수 있는 벌통 개수, C: 꿀을 채취할 수 있는 최대 양
    # 2명의 일꾼으로 고정
    honey = [list(map(int, input().split())) for _ in range(N)]
    newh = [[0]*(N-M+1) for _ in range(N)]
    toth = 0
    maxH = 0
    secH = 0
    for i in range(N):
        for j in range(N-M+1):
            A = honey[i][j:j+M]
            ggool(A, i, j)
    print(newh)
    for hi in range(N):
        for hj in range(N-M+1):
            if maxH < newh[hi][hj]:
                maxH = newh[hi][hj]
                mi, mj = hi, hj

    for hi in range(N):
        for hj in range(N-M+1):
            if mi == hi and abs(mj-hj) > M-1:
                if secH < newh[hi][hj] <= maxH:
                    secH = newh[hi][hj]
            elif mi != hi:
                if secH < newh[hi][hj] <= maxH:
                    secH = newh[hi][hj]
    print('#{0} {1}'.format(tc+1, maxH+secH))
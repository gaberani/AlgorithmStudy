def f(n, cnt):
    global result
    if n > len(chi):
        return
    if cnt == M:
        min_d = 0
        for h in home:      # 집마다
            HtoC = N*10
            for v in visit:   # 찍은 치킨 집들 중
                c = chi[v]
                distance = abs(h[0]-c[0]) + abs(h[1]-c[1])
                if HtoC > distance:
                    HtoC = distance     # 가장 짧은 거리 구함.
            min_d += HtoC       # 치킨 거리에 더해줌
        if result > min_d:
            result = min_d      # 그 때의 치킨 거리 최솟값 갱신
        return
    visit.append(n)
    f(n+1, cnt+1)
    visit.pop()
    f(n+1, cnt)

N, M = map(int, input().split())
dosi = [list(map(int, input().split())) for _ in range(N)]
home, chi = [], []
for i in range(N):
    for j in range(N):
        if dosi[i][j] == 1:
            home.append([i, j])
        elif dosi[i][j] == 2:
            dosi[i][j] = 0
            chi.append([i, j])

visit = list()
result = 2**31-1
f(0, 0)
print(result)

# 조합 내장 함수 코드
'''
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
'''

# 시간 초과 (Try 1)
''' 
def f(n, k):
    global result
    if n == k:
        minD = 0
        for h in home:      # 집마다
            HtoC = N*2
            for p in livechi:   # 찍은 치킨 집들 중
                distance = abs(h[0]-p[0]) + abs(h[1]-p[1])
                if HtoC > distance:     # 가장 짧은 거리
                    HtoC = distance
            minD += HtoC            # 치킨 거리에 더해줌
        if result > minD:     # 치킨 거리 최솟값 갱신
            result = minD
    else:
        for i in range(n, len(chi)):
            if not visit[i] and (i == 0 or chi[i-1] != chi[i] or visit[i-1]):
                visit[i] = 1
                livechi[n] = chi[i]
                f(n+1, k)
                visit[i] = 0

N, M = map(int, input().split())
dosi = [list(map(int, input().split())) for _ in range(N)]
home = []
chi = []
for i in range(N):
    for j in range(N):
        if dosi[i][j] == 1:
            home.append([i, j])
        elif dosi[i][j] == 2:
            dosi[i][j] = 0
            chi.append([i, j])

result = 2*31-1
visit = [0]*len(chi)
livechi = [0]*M
f(0, M)
print(result)
'''
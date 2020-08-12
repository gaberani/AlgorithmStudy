def dfs(n, k, money):
    global minV
    if n >= k:      # 넘으면 앞에까지만, 같으면 그 날짜까지 포함해서 더하기
        if n == k:
            if maxV < sum(money):
                maxV = sum(money)
                # money = []
                return
        else:       # 날짜를 넘으면
            if maxV < sum(money[:-1]):
                maxV = sum(money[:-1])
                # money = []
                return
    else:
        for i in range(n, N):  # 시작점 1일부터 N일까지 잡아서 해보기
            money.append(P[i])
            dfs(i+T[i], N, money)
            money.pop()

N = int(input())
T = [0]*N
P = [0]*N
for index in range(N):
    T[index], P[index] = list(map(int, input().split()))

money = []
minV = 0
dfs(0, N, [])
print(minV)
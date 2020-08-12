def dfs(start, visited, money):
    global minV
    visited.append(start)
    for i in range(N):
        if path[start][i] == 1 and i not in visited:    
            money.append(dosi[start][i])
            dfs(i, visited, money)
            money.pop()
            visited.pop()
    if len(visited) == N:
        cost = sum(money) + dosi[start][visited[0]]     # 처음 도시로 돌아오는 길은 무조건 고정이므로
        if dosi[start][visited[0]] == 0:        # 돌아오는 길이 0이라 갈 수 없는 길이라면
            return                              # 불가능하므로 돌려보냄!
        if minV > cost:                         # 아니면 비교해서 
            minV = cost                         # 최소값 갱신

N = int(input())
dosi = [list(map(int, input().split())) for _ in range(N)]
path = [[0]*N for _ in range(N)]
minV = 0
for i in range(N):
    for j in range(N):
        minV += dosi[i][j]
        if dosi[i][j] != 0:
            path[i][j] = 1

for i in range(N):
    money = []
    visited = []
    dfs(i, visited, money)
print(minV)
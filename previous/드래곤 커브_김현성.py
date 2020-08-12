import pprint
di = [0, -1,  0, 1]
dj = [1,  0, -1, 0]  # 우상좌하

def curve(X, Y, D, G):
    i, j = Y, X
    grid[i][j] = 1              # 0세대 커브
    dstack = [D]

    # g만큼 반복해서 커브 만듬
    for g in range(G):    # 1부터 G까지 세대 방향 만듬
        tmp_D = dstack
        # 이전 세대 방향(dstack) 을 +1 한 뒤 역순으로 다음 세대 방향(tmp_D)에 붙임
        for nd in range(len(dstack)-1, -1, -1):
            tmp_D.append((dstack[nd]+1) % 4)
        dstack = tmp_D

    # 그리드에 표시하기
    for d in dstack:
        i += di[d]
        j += dj[d]
        grid[i][j] = 1


N = int(input())                        # N:드래곤 커브 개수
grid = [[0]*101 for _ in range(101)]    # 격자판
for _ in range(N):
    # (X, Y): 시작점 / D: 시작방향 / G: 세대
    X, Y, D, G = map(int, input().split())
    curve(X, Y, D, G)

# pprint.pprint(grid)

# 결과값
result = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1:
            if grid[i+1][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] == 1:
                result += 1
print(result)
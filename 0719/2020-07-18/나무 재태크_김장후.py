import sys; input = sys.stdin.readline
from collections import deque


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
food = [[5] * N for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

year = 0
while year < K:
    dead = deque()
    tree_five = deque()
    # sping
    for r in range(N):
        for c in range(N):
            if tree[r][c]:
                cnt = 0
                cnt_tree = len(tree[r][c])
                while cnt < cnt_tree:
                    ta = tree[r][c].popleft()
                    if food[r][c] >= ta:
                        food[r][c] -= ta
                        ta += 1
                        if not (ta%5):
                            tree_five.append((r, c))
                        tree[r][c].append(ta)
                    else:
                        dead.append((r, c, ta//2))
                    cnt += 1

    # summer
    while dead:
        x, y, value = dead.popleft()
        food[x][y] += value

    # fall
    while tree_five:
        tr, tc = tree_five.popleft()
        for k in range(8):
            nr = tr + di[k]
            nc = tc + dj[k]
            if 0 <= nr < N and 0 <= nc < N:
                tree[nr][nc].appendleft(1)

    # winter
    for r in range(N):
        for c in range(N):
            food[r][c] += A[r][c]

    year += 1


answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)

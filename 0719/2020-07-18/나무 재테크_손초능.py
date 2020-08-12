from collections import deque
import sys
input = sys.stdin.readline

n, num_tree, years = map(int, input().split())
mineral = [[5]*n for _ in range(n)]
add = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(num_tree):
    x, y, age = map(int, input().split())
    trees[x-1][y-1].appendleft(age)

for _ in range(years):
    #
    # for i in range(n): print(trees[i])

    cnt = 0
    add_mineral = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                new_tree, flag = deque(), 1
                for age in trees[i][j]:
                    if flag and mineral[i][j]>=age:
                        mineral[i][j] -= age
                        new_tree.append(age+1)
                    else:
                        flag = 0
                        add_mineral[i][j] += age//2
                trees[i][j] = new_tree.copy()

    for i in range(n):
        for j in range(n):
            if not trees[i][j]: cnt += 1
            else:
                for age in trees[i][j]:
                    if age%5 == 0:
                        for k in range(8):
                            x, y = i+dx[k], j+dy[k]
                            if 0<=x<n and 0<=y<n:
                                trees[x][y].appendleft(1)

    if cnt == n**2: break

    for i in range(n):
        for j in range(n):
            mineral[i][j] += add[i][j]+add_mineral[i][j]

result = 0
for i in range(n):
    for j in range(n):
        result += len(trees[i][j])
print(result)
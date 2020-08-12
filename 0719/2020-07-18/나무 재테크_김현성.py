from collections import deque
# import time
# start = time.time()
N, M, K = map(int, input().split())

s2d2 = [list(map(int, input().split())) for _ in range(N)]
grid = [[5]*N for _ in range(N)]
tree_dict = {(i//N, i%N): deque() for i in range(N*N)}

di = [0,  0, 1, 1,  1, -1, -1, -1]
dj = [1, -1, 1, 0, -1,  1,  0, -1]

for _ in range(M):
    x, y, age = list(map(int, input().split()))
    tree_dict[(x-1, y-1)].append(age)

for _ in range(K):
    # 봄, 여름 동시에 처리
    for (i, j), trees in tree_dict.items():
        tmp_trees = deque()
        dead_sum = 0
        for tyear in trees:
            # 봄
            if tyear <= grid[i][j]:
                grid[i][j] -= tyear
                tmp_trees.append(tyear+1)
            # 여름
            else:
                dead_sum += tyear//2
        tree_dict[(i, j)] = tmp_trees
        grid[i][j] += dead_sum

    # 가을
    new_tree = []
    for (i, j), trees in tree_dict.items():
        for tyear in trees:
            if tyear%5 == 0:
                for d in range(8):
                    ni, nj = i+di[d], j+dj[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        new_tree.append((ni, nj))
    for i, j in new_tree:
        tree_dict[(i, j)].appendleft(1)

    # 겨울
    for i in range(N*N):
        ni, nj = i//N, i%N
        grid[ni][nj] += s2d2[ni][nj]

result = 0
for trees in tree_dict.values():
    result += len(trees)
print(result)
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
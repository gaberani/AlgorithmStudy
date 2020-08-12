import sys
import pprint
from collections import deque
N, M, K = map(int, sys.stdin.readline().split())
# 나무 양분 정보
food = [[5]*N for _ in range(N)]
# 추가되는 나무 양분 정보
new_food = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 기존 나무 나이 정보
A = [[[]*N for _ in range(N)] for _ in range(N)]

# 새로운 나무 정보
for _ in range(M):
    # x: 나무 열, y: 나무 행, z: 나무 나이
    x, y, z = list(map(int, sys.stdin.readline().split()))
    A[x-1][y-1].append(z)
    A[x-1][y-1].sort()

# K년간 반복
num = M
for _ in range(K):
    # 1. 봄
    print(A)
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                dead_tree = 0
                # 여러 나무가 있다면 어린 나무부터
                for t in range(len(A[r][c])):
                    # 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가
                    if food[r][c] >= A[r][c][t]:
                        food[r][c] -= A[r][c][t]
                        A[r][c][t] += 1
                    # 양분이 자신의 나이만큼 없는 경우 죽음
                    else:
                        # 2. 여름
                        for v in range(t, len(A[r][c])):
                            # 여름에 양분으로 변함
                            # 죽은 나무의 나이를 2로 나눈 값이 양분으로 추가, 소수점 버림
                            dead_tree += A[r][c][v]//2
                            # 나무 나이 정보 제거
                            num -= 1
                        A[r][c] = A[r][c][:t]
                        break
                # 2. 여름
                # 양분 추가
                food[r][c] += dead_tree

    # 3. 가을 - 번식
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                for tree in A[r][c]:
                    # 나이가 5의 배수인 나무
                    if not tree % 5:
                        # 8방향
                        dr, dc = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]
                        for k in range(8):
                            nr, nc = r+dr[k], c+dc[k]
                            # 땅을 벗어나는 칸에는 나무가 안생긴다.
                            # 인접한 8개의 칸에 나이가 1인 나무가 생김
                            if 0 <= nr < N and 0 <= nc < N:
                                A[nr][nc].insert(0, 1)
                                num += 1
    # 4. 겨울 - 양분 추가
    for r in range(N):
        for c in range(N):
            food[r][c] += new_food[r][c]
        # 각 칸에 추가되는 양분의 양은 new_food[r][c]=> 입력으로 주어짐

# 살아남은 나무 수 출력
print(num)




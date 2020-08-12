import pprint

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]     # 우상 / 우하 / 좌하 / 좌상

N = int(input())  # 한 줄의 크기
toopyo = [list(map(int, input().split())) for _ in range(N)]  # 선거구
minV = 2**31-1

total_sum = 0
for i in range(N):
    total_sum += sum(toopyo[i])

for x in range(0,N-2):
    for y in range(1, N-1):
        for d1 in range(1, y+1):
            for d2 in range(1, N-y):
                sum_1 = 0
                for i in range(0, x+d1):
                    for j in range(0, y+1):
                        if 0 <= i < N and 0 <= j < N:
                            sum_1 += toopyo[i][j]
                # 5구역에 해당하는 곳 제외
                t = -1
                for i in range(x, x+d1):
                    t = t + 1
                    for j in range(y-t, y+1):
                        if 0 <= i < N and 0 <= j < N:
                            sum_1 -= toopyo[i][j]

                sum_2 = 0
                for i in range(0, x+d2+1):
                    for j in range(y+1, N):
                        if 0 <= i < N and 0 <= j < N:
                            sum_2 += toopyo[i][j]
                # 5구역에 해당하는 곳 제외
                t = 0
                for i in range(x+1, x+d2+1):
                    t = t + 1
                    for j in range(y+1, y+1+t):
                        if 0 <= i < N and 0 <= j < N:
                            sum_2 -= toopyo[i][j]

                sum_3 = 0
                for i in range(x+d1, N):
                    for j in range(0, y-d1+d2):
                        if 0 <= i < N and 0 <= j < N:
                            sum_3 += toopyo[i][j]
                # 5구역 제외
                t = -1
                for i in range(x+d1, x+d1+d2+1):
                    t = t + 1
                    for j in range(y-d1+t, y-d1+d2):
                        if 0 <= i < N and 0 <= j < N:
                            sum_3 -= toopyo[i][j]

                sum_4 = 0
                for i in range(x+d2+1, N):
                    for j in range(y-d1+d2, N):
                        if 0 <= i < N and 0 <= j < N:
                            sum_4 += toopyo[i][j]
                # 5구역 제외
                t = -1
                for i in range(x+d2+1, x+d2+d1+1):
                    t = t + 1
                    for j in range(y-d1+d2, y+d2-t):
                        if 0 <= i < N and 0 <= j < N:
                            sum_4 -= toopyo[i][j]
                not5 = sum_1 + sum_2 + sum_3 + sum_4
                newV = max(sum_1, sum_2, sum_3, sum_4, total_sum-not5) - min(sum_1, sum_2, sum_3, sum_4, total_sum-not5)
                if minV > newV:
                    minV = newV
print(minV)


# way 1

# def divide(i, j, d, visit):
#     if d == 3 and sp == [i, j]:  # 선거구 확정되는 조건
#         # 선거구 인구 차이의 최솟값 구하기
#         pprint.pprint(visit)
#         find(visit)
#     elif 0 <= i <= N-1 and 0 <= j <= N-1 and visit[i][j] == 0:
#         if d != 3:
#             visit[i][j] = 1
#             divide(i+di[d+1], j+dj[d+1], d+1, visit)
#             visit[i][j] = 0
#         visit[i][j] = 1
#         divide(i+di[d], j+dj[d], d, visit)
#         visit[i][j] = 0
#
# def find(visit):
#     global minV
#     min_i, max_i, min_j, max_j = N-1, 0, N-1, 0
#     for i in range(N):
#         for j in range(N):
#             if visit[i][j] == 1:
#                 min_i = i if min_i > i else min_i
#                 max_i = i if max_i < i else max_i
#                 min_j = j if min_j > j else min_j
#                 max_j = j if max_j < j else max_j
#     print(min_i, max_i, min_j, max_j)
#
#     num1 = 0
#     num2 = 0
#     num3 = 0
#     num4 = 0
#     num5 = 0
#     for i in range(N):
#         for j in range(N):
#             if j < max_j and i <= min_i:
#                 visit[i][j] = 1
#             if j >= max_j and i < max_i:
#                 visit[i][j] = 2
#             if j <= min_j and i > min_i:
#                 visit[i][j] = 3
#             if j > min_j and i <= max_i:
#                 visit[i][j] = 4
#             if min_i <= i <= max_i and min_j <= j <= max_j:
#                 visit[i][j] = 5
#     pprint.pprint(visit)
#     newV = max(num1, num2, num3, num4, num5) - min(num1, num2, num3, num4, num5)
#     if minV > newV:
#         minV = newV
#
# N = int(input())  # 한 줄의 크기
# toopyo = [list(map(int, input().split())) for _ in range(N)]  # 선거구
# minV = 2**31-1
# for si in range(N):
#     for sj in range(N):
#         sp = [si, sj]
#         visit = [[0]*N for _ in range(N)]
#         divide(si, sj, 0, visit)
# print(minV)
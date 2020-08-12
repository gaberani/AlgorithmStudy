def color(result_lst, n, cost):
    for i in range(1, n):
        # 각각 첫 집 이 R, G, B 칠하고 시작한 것
        result_lst[i][0] = cost[i][0] + min(result_lst[i-1][1], result_lst[i-1][2])
        result_lst[i][1] = cost[i][1] + min(result_lst[i-1][0], result_lst[i-1][2])
        result_lst[i][2] = cost[i][2] + min(result_lst[i-1][0], result_lst[i-1][1])
        print(result_lst)
    min_val = min(result_lst[n-1][0], result_lst[n-1][1], result_lst[n-1][2])
    return min_val

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
result_lst = [[-1] * 3 for _ in range(n)]
for h in range(3):
    result_lst[0][h] = cost[0][h]  # R
print(color(result_lst, n, cost))
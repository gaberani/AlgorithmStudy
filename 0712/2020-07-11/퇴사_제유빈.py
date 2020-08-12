# 2020-07-10 다시풀기
import sys
def dfs(day, profit):
    global N, max_profit
    # N번째 날이면
    if day == N:
        # 최댓값보다 큰 경우 갱신
        if profit > max_profit:
            max_profit = profit
    else:
        # 다음 예약 가능한 날짜 탐색
        for i in range(day+P[day][0], N+1):  # day+P[day][0]: 이전 상담일 + 지속일
            # 다음 예약이 끝나는 날짜가 N+1보다 작거나 같으면
            if i + P[i][0] <= N+1:
                # 예약 가능
                dfs(i, profit+P[i][1])
        # 다음 예약 가능한 날짜 없으면
        else:
            # 최댓값인 경우 갱신
            if profit > max_profit:
                max_profit = profit

N = int(sys.stdin.readline())
P = [[0]*2]+[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_profit = 0

# 예약 시작일
for t in range(1, N+1):
    # 예약 끝나는 날짜가 마지막 날+1 보다 작거나 같으면
    if t+P[t][0] <= N+1:
        dfs(t, P[t][1])
print(max_profit)


# 0. 인풋 정리
N = int(input())
# 기간, 금액
T, P = [0]*N, [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())

dp = [0]*20
for i in range(N):
    if dp[i] > dp[i+1]:  # 오늘이 내일보다 보상이 높다면
        dp[i+1] = dp[i]  # 내일 보상을 오늘 금액을 넣음
    if dp[i+T[i]] < dp[i] + P[i]:  # T일 후에 받게될 금액이 오늘의 금액보다 더 큼
        dp[i+T[i]] = dp[i] + P[i]  # T일 후에 받을 금액을 넣는다.

print(dp[N])
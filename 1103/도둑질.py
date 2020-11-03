# 각 집들은 서로 인접한 집들과 방범장치가 연결되어 있기 때문에
# 인접한 두 집을 털면 경보가 울립니다.

# 각 집에 있는 돈이 담긴 배열 money가 주어질 때,
# 도둑이 훔칠 수 있는 돈의 최댓값을 return
def solution(money):
    dp = [0]*len(money)
    dp[0], dp[1] = money[0], max(money[0], money[1])

    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], money[i]+dp[i-2])
    val = max(dp)

    dp = [0]*len(money)
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i-1], money[i]+dp[i-2])

    return max(val, max(dp))

print(solution([1, 2, 3, 1]))
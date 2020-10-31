# 각 집에 있는 돈이 담긴 배열 money가 주어질 때,
# 도둑이 훔칠 수 있는 돈의 최댓값을 return
def solution(money):
    answer = 0
    dp = [0]*len(money)
    dp[0], dp[1] = money[0], money[1]

    return answer
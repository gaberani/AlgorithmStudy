G = int(input())
stairs = [0]*301
for i in range(G):
    stairs[i] = int(input())

# 연속된 세 개의 계단을 모두 밟아서는 안 된다
#       1               1+1                     1+2                 2+1
dp = [0]*301
dp[0] = stairs[0]
dp[1] = stairs[0]+stairs[1]
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, G):
    dp[i] = max(stairs[i-1]+stairs[i]+dp[i-3], stairs[i]+dp[i-2])
print(dp[G-1])
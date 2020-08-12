N = int(input())
A = list(map(int, input().split()))
dp = [1]*N # 자기 자신 미리 세서 1
# 각각 자리에서 자신보다 크면 세기
for i in range(N):
    for j in range(i, N):
        if A[j] > A[i]:
            dp[i] += 1
            A[i] = A[j]
print(dp)
print(max(dp))
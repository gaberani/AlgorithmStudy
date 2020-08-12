N = int(input())
A = list(map(int, input().split()))
# A 배열의 각 인덱스의 수로 끝나는 부분 수열의 최장 길이 저장
cnt = [1]*N
for i in range(1, N):
    # A[i]보다 작은 값으로 끝나는 부분 수열 중 가장 긴 길이 저장 
    tmp = 0
    for j in range(i):
        if A[i] > A[j] and tmp < cnt[j]:
            tmp = cnt[j]
    cnt[i] += tmp
print(max(cnt))
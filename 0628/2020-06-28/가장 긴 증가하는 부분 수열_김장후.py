import sys; input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
tmp = [0] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and tmp[i] < tmp[j]:
            tmp[i] = tmp[j]
    tmp[i] += 1
print(max(tmp))



# 6
# 10 20 10 30 20 50
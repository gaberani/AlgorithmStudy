n = int(input())
arr = list(map(int, input().split()))
length = [0]*n
length[0] = 1
for i in range(1, n):
    cnt = 0
    for j in range(i):
        if arr[j] < arr[i] and length[j] > cnt:
            cnt = length[j]
    length[i] = cnt + 1
print(sum(length))
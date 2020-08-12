n = int(input())
arr = [[1]*2 for _ in range(n+1)]
for i in range(1, n+1):
    arr[i][0], arr[i][1] = map(int, input().split())
q = [[0, 0]]
max_p = 0
while q:
    day, punish = q.pop(0)
    max_p = max(punish, max_p)
    for d in range(day+arr[day][0], n+1):
        if d+arr[d][0]-1 <= n:
            q.append([d, punish+arr[d][1]])
print(max_p)
n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
# print(tri)
# 맨 왼쪽이면 무조건 자신 오른쪽 위를 더함

for i in range(1, n):   # 첫번째 줄은 뺌
    for j in range(i+1):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
print(max(tri[n-1]))
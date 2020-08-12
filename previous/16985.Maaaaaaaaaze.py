# 결과값은 무조건 12이상이다. (최소값이 12다)
import pprint

# 회전 횟수 뽑기
def f(n, k):
    if n == k:
        print(p)
    else:
        for i in range(4):
            p[n] = i
            f(n+1, k)

# 90도 회전
def quarter():
    pass

# 미로


# 3차원 배열 받기(1: 들갈 수 있는 칸)
miro = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
pprint.pprint(miro)

p = [0]*5
# 회전 가능한 경우의 수 뽑기
f(0, 5)

# 미로 가능한 시작점 찾아서 보냄
for i in range(5):
    for j in range(5):
        if miro[0][i][j] == 1:
            pass

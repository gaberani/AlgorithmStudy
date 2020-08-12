n = int(input())
wines = []
wine = []
for _ in range(n):
    a = int(input())
    # [현재 위치 포도주를 마셨을 때 최대 양, 안 마셨을 때 최대양 ]
    wines.append([a, 0])
    # 포도주 양 저장
    wine.append(a)
if n>=2:
    # 두번째 포도주 정보 저장
    wines[1] = [wine[0]+wine[1], wine[0]]
for i in range(2, n):
    # i번째 포도주를 마신다고 할 때, (i-1 포도주를 마시지 않았을 때, i-2 포도주를 마시지 않고 i-1 포도주를 마셨을 때)의 최대값 비교
    wines[i][0] += max(wines[i-1][1], wines[i-2][1]+wine[i-1])
    # i번째 포도주를 안 마신다고 할 때, (i-1포도주 마실 때, 안 마실 때) 최대값 비교
    wines[i][1] += max(wines[i-1])
print(max(wines[-1]))
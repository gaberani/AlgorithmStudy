N = int(input())
A = list(map(int, input().split()))     # 각 시험장에 있는 응시자 수
B, C = map(int, input().split())
# B : 총감독관이 한 방에서 감시할 수 있는 응시자 수 / C : 부감독관이 한 방에서 감시할 수 있는 응시자 수
# 방마다 총감독관은 1명, 부감독관은 여러명 가능

result = 0
for i in range(N):
    num = A[i]
    if num >= B:
        num -= B
        gamdok = 1
        nanu1 = num / C
        mok = num // C
        if nanu1 != mok:
            mok += 1
        gamdok += mok
        result += gamdok
    else:
        result += 1
print(result)
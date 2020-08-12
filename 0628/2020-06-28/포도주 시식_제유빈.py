import sys

N = int(sys.stdin.readline())
# 포도주 양
W = [int(sys.stdin.readline()) for _ in range(N)]
if N == 1:       # 포도주를 1잔 마시는 경우
    print(W[0])  # 첫 번째 값 출력
    sys.exit()   # 종료

# 마실 수 있는 포도주 양
P = [0, W[0], W[0]+W[1]]+[0]*(N-2)  # 0, 1, 2개 설정 후
for i in range(3, N+1):
    P[i] = max(W[i-1]+P[i-2], W[i-1]+W[i-2]+P[i-3], P[i-1])
print(P[N])

    


# LIS
import sys

def LIS(L):
    global N
    # array of maximum lengths till the point
    T = [0]*N
    for i in range(N):
        T[i] = 1     # default length
        # investigate former points
        for j in range(i):
            if L[j] < L[i]:   # if increased
                T[i] = max(T[i], 1+T[j])
    # return max(T)
    max_idx = 0
    for i in range(1, N):
        if T[i] > T[max_idx]:
            max_idx = i
    return T[max_idx]

# length of the sequence
N = int(sys.stdin.readline())
# array of the sequence
L = list(map(int, sys.stdin.readline().split()))

print(LIS(L))



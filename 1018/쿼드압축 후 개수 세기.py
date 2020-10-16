def solution(arr):
    answer = []
    L = len(arr)
    N = 0
    while L > 1:
        L //= 2
        N += 1

    for binary in range(N):
        start = arr[N-binary][N-binary]
        for i in range(binary**2):
            for j in range(binary**2):
                pass

    return answer
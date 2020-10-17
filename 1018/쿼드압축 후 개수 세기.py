def solution(arr):
    answer = []
    L = len(arr)
    N = 0
    # 행렬의 길이가 2의 몇 제곱인지 구하기
    while L > 1:
        L //= 2
        N += 1

    # 시작점 설정을 어떻게 해야할지 고민이 더 필요하다
    for binary in range(N):
        start = arr[N-binary][N-binary]
        for i in range(binary**2):
            for j in range(binary**2):
                pass

    return answer

def solution(key, lock):
    ans, M, N = True, len(key), len(lock)

    def rotate(key):     # 90도 회전해서 리턴
        nonlocal M
        R = [[0]*M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                R[i][j] = key[M-j-1][i]
        return R

    def check(r, c, key):   # 각 점에서 배정 가능한지 확인
        nonlocal M, N, lock
        # 확인을 위한 배열을 만듬 (가운데에 Lock이 놓인 배열)
        P = [[0]*(N+2*M-2) for _ in range(N+2*M-2)]
        for i in range(N):
            for j in range(N):
                P[i+M-1][j+M-1] = lock[i][j]

        L = len(P)
        # 자물쇠를 놓고 싶은 지점에 확인
        for i in range(M):
            for j in range(M):
                if key[i][j]:             # key에 돌기가 있고
                    if not P[i+r][j+c]:   # 자물쇠는 홈이 있으면
                        P[i+r][j+c] = 1   # 표시
                    else:                 # 자물쇠도 돌기가 있으면
                        return False      # 자물쇠를 열 수 없음 !

        # 자물쇠를 놓은 경우 검사
        for row in range(M-1, N+M-1):
            if P[row][M-1:N+M-1] != [1]*N:   # 홈이 채워지지 않은 행이 있으면 열 수 없음
                return False
        return True

    # 네 방향 검사를 위한 range
    for _ in range(4):
        # 홈의 가능한 시작 지점 찾기 (P에 놓는다 가정)
        for r in range(N+M-1):
            for c in range(N+M-1):
                ans = check(r, c, key)
                # True 이면 return
                if ans:
                    return ans
        # 모든 점에 놓을 수 없으면 회전한 후 검사한다.
        key = rotate(key)
    return ans


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))


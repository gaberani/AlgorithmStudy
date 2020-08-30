import copy
def solution(key, lock):
    # lock을 시계 방향으로 회전시키는 함수
    def rotate(arr):
        tmp = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # tmp[i][j] = arr[i][M-j-1]
                tmp[i][j] = arr[N-j-1][i]
        return tmp

    # key로 lock을 풀 수 있는지 체크하는 함수
    def check(arr, si, sj):
        cnt = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0 and key[si+i][sj+j] == 1:
                    cnt += 1
                # 열쇠의 돌기와 자물쇠의 돌기 겹치는지 체크
                elif arr[i][j] == 1 and key[si+i][sj+j] == 1:
                    return -1
        return cnt

    # M은 항상 N 이하 ( M <= N )
    N, M = len(lock), len(key)  # lock의 길이, key의 길이
    hole_cnt = 0  # lock의 홈 개수
    for i in range(N):
        hole_cnt += lock[i].count(0)

    # 1. key와 lock 길이 확인해서 key를 넓힌다.
    for i in range(M):
        key[i] = [0]*(N-1) + key[i] + [0]*(N-1)
    zero = []
    for _ in range(2*N+M-2):
        zero += [0]
    for i in range(N-1):
        key += [copy.deepcopy(zero)]        # 위
        key = [copy.deepcopy(zero)] + key   # 아래

    # 2. 새로 만든 key에 lock을 돌리면서 확인
    for _ in range(4):
        for i in range(N+M-1):          # key의 시작점 i
            for j in range(N+M-1):      # key의 시작점 j
                if hole_cnt == check(lock, i, j):
                    print(i, j)
                    return True
        lock = rotate(lock)
    return False
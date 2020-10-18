def solution(arr):
    answer = []
    L = len(arr)
    N = 0
    while L > 1:
        L //= 2
        N += 1

    tmp = []
    def dfs(si, sj, cnt):
        start = arr[si][sj]
        for i in range(si, si+2**cnt):
            for j in range(sj, sj+2**cnt):
                if arr[i][j] != start:
                    dfs(si, sj, cnt-1)
                    dfs(si, sj+2**(cnt-1), cnt-1)
                    dfs(si+2**(cnt-1), sj, cnt-1)
                    dfs(si+2**(cnt-1), sj+2**(cnt-1), cnt-1)
                    return
        # 전부 시작값과 같으면 숫자 하나로 압축
        tmp.append(start)

    dfs(0, 0, N)
    answer = [tmp.count(0), tmp.count(1)]
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
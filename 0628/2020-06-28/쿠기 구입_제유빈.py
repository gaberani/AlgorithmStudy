def solution(cookie):
    ans = 0   # 최댓값 저장
    N = len(cookie)
    # 분기점 m
    for m in range(N-1):
        # 인덱스, 값 저장
        idx, sons = [m, m+1], [cookie[m], cookie[m+1]]
        while True:
            if sons[0] == sons[1]:   # 값이 같을 때
                if ans < sons[0]:    # 더 크면 저장
                    ans = sons[0]
            if sons[0] < sons[1]:   # 첫째 값이 더 작을때
                if idx[0]:              # 인덱스 있으면 이동
                    idx[0] -= 1
                    sons[0] += cookie[idx[0]]
                    continue
                break
            else:
                if idx[1] < N-1:
                    idx[1] += 1
                    sons[1] += cookie[idx[1]]
                    continue
                break
    return ans
    

print(solution([1, 1, 2, 3]))   # 3
print(solution([1, 2, 4, 5]))   # 0
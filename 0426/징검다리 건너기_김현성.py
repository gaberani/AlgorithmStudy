import timeit
start = timeit.default_timer()

def solution(stones, k):
    answer = 0
    Ls = len(stones)
    while 1:
        cnt = 0
        for i in range(Ls):
            if stones[i] <= 0:
                cnt += 1
            else:
                if cnt >= k:
                    return answer
                cnt = 0
            if cnt >= k:
                    return answer
            stones[i] -= 1
        answer += 1
    return answer

stop = timeit.default_timer()
print(stop - start)
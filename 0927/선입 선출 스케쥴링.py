# CPU에는 여러 개의 코어가 있고, 코어별로 한 작업을 처리하는 시간이 다릅니다.
# 한 코어에서 작업이 끝나면 작업이 없는 코어가 바로 다음 작업을 수행합니다.
# 2개 이상의 코어가 남을 경우 앞의 코어부터 작업을 처리 합니다.

# 처리해야 될 작업의 개수 n / 각 코어의 처리시간이 담긴 배열 cores
def solution(n, cores):
    # 마지막 작업을 처리하는 코어의 번호를 return
    answer = 0
    L = len(cores)
    idx = L-1
    process = [0]*L
    while 1:
        for i in range(L):
            process[i] += 1
            if process[i] == cores[i]:
                idx += 1
                process[i] = 0
            if idx == n-1:
                answer = i+1
                break
        if idx == n-1:
            break
    return answer

# print(solution(6, [1,2,3]))
# print(solution(8, [1,2,3]))


def solution1(n, cores):
    answer = 0
    job = [0]*50000
    job_idx, tmp_idx = len(cores)-1, 0
    while job_idx < 50001:
        print(job)
        for core in range(len(cores)):
            print(job_idx, cores[core], job_idx%cores[core])
            if job_idx%cores[core] == 0:
                job[job_idx+tmp_idx] = core
                tmp_idx += 1
        job_idx, tmp_idx = job_idx+tmp_idx, 0
        print('-----------------------------------------')
    return answer

print(solution1(6, [1,2,3]))
print(solution1(8, [1,2,3]))
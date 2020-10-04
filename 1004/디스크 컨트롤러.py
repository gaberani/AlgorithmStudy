import heapq

def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: (x[0], x[1]))
    # 처음엔 가장 먼저 들어온 가장 짧은 작업으로 시작
    start, time = jobs.pop(0)
    end = start + time
    answer = answer + time
    while jobs:
        next_i = 0
        # 시작 인덱스는 제외하고 탐색
        for i in range(1, len(jobs)):
            if jobs[i][0] > end:
                break
            else:
                if jobs[i][1] < jobs[next_i][1]:
                    next_i = i
        next_job = jobs.pop(next_i)
        # 다음 할 일이 대기중
        if next_job[0] <= end:
            # 대기 시간 만큼 더해줌
            answer = answer + next_job[1] + (end - next_job[0])
            end = end + next_job[1]
        # 다음 할 일이 대기중이 아닐 경우
        else:
            # 대기 시간이 없었으므로 작업시간 만큼만 더해줌
            answer = answer + next_job[1]
            end = sum(next_job)
    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[1, 3], [1, 9], [2, 6]]))
print(solution([[0, 4], [0, 3], [0, 2], [0, 1]]))
print(solution([[0, 3], [1, 9], [2, 6], [20, 3]]))
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))


# 시간을 1씩 더하면서 풀어도 가능
def solution1(jobs):
    answer = 0
    disk, time, past = [], 0, -1
    cnt = 0
    while cnt < len(jobs):
        # 할 일 찾기
        for job in jobs:
            if past < job[0] <= time:
                answer += (time-job[0])
                heapq.heappush(disk, job[1])
        # 요청된 것이 없을 경우
        if not disk:
            time += 1
        # 이미 요청된 것들이 있을 경우(디스크에 할 일 존재)
        else:
            answer += len(disk)*disk[0]
            past = time
            time += heapq.heappop(disk)
            cnt += 1
    return answer

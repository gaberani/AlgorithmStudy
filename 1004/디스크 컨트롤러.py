import heapq

def solution(jobs):
    # 작업의 요청부터 종료까지 걸린 시간의 평균 return
    answer = 0
    L = len(jobs)

    # 1. 작업 시간이 더 짧은 것
    # 2. 요청 시간이 먼저 들어온 것
    heap = []
    for req, com in jobs:
        heapq.heappush(heap, (com, req))

    pre, now = 0, heap[0][1]
    # 하드디스크가 작업을 수행하고 있지 않을 때, 먼저 요청이 들어온 작업부터 처리
    while heap:
        com, req = heapq.heappop(heap)


    return answer // L


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[1, 3], [1, 9], [2, 6]]))
print(solution([[0,4], [0,3], [0,2], [0,1]]))
print(solution([[0, 3], [1, 9], [2, 6], [20, 3]]))
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))

def solution1(jobs):
    answer = 0
    memory, time = [], 0

    while jobs:
        # 요청된 것이 없을 경우
        if not memory:
            minT = 2 ** 31 - 1
            for jIdx in range(len(jobs)):
                if jobs[jIdx][1] < minT:
                    minT, minIdx = jobs[jIdx][1], jIdx
        # 이미 요청된 것들이 있을 경우(메모리 존재)
        else:
            # 메모리 내에서 찾기
            for mIdx in range(len(memory)):
                min

    return answer
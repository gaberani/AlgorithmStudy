# 입국심사를 기다리는 사람 수 n
# 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times

# 그리디
def solution(n, times):
    # 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return
    answer, cnt = 0, 0
    L = len(times)
    simsa = [0]*L
    waiting = []
    waitsim = []
    while 1:
        # 1분 씩 더하기 & 심사완료 여부
        for i in range(L):
            # 대기해야하는 심사관 아니면 더하기
            if i not in waitsim:
                simsa[i] += 1
            # times와 일치하면 심사 완료
            if simsa[i] == times[i]:
                simsa[i] = 0

        # 손님 기다릴지 보낼지 여부
        # 먼저 기다리는 손님 있다면
        if waiting:
            for waitone in waiting:
                waitsim
        # 남는 심사관 체크
        for i in range(L):
            pass
            # 만약 기다렸다가 다른 심사원에게 받는게 빠르면 대기 시키기

        # 심사 끝날 때까지 걸리는 시간
        answer += 1
        if cnt == n:
            break
    return answer

# print(solution(6, [7, 10])) # 28
# print(solution(7, [7, 10])) # 30

# 이분 탐색
def solution1(n, times):
    # answer = 0
    left, right = 1, max(times)*n
    # left를 1*n이라고 두면 틀림 왜징
    # 처음에 시작할 때 심사관 수 만큼 들어가고 시작하기 때문!!
    while left < right:
        # 총 걸리는 시간 mid, 심사관 마다 할 수 있는 사람 수 더하는 cnt
        mid = (left + right)//2
        cnt = 0
        # 심사관 마다 총 걸리는 시간안에 소화 가능한 사람 더하기
        for simsa in times:
            cnt += mid // simsa
        if cnt < n:
            left = mid + 1
        else:
            right = mid
    return left


print(solution1(6, [7, 10])) # 28
print(solution1(7, [7, 10])) # 30
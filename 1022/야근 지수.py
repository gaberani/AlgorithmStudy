# 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값
# Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.
# Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때,

# 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해
# 야근 피로도를 최소화한 값을 리턴하는 함수 solution
def solution1(n, works):
    while n != 0:
        max_work = max(works)
        max_idx = works.index(max_work)
        works[max_idx] -= 1
        n -= 1
    answer = sum(w ** 2 for w in works)
    return answer

def solution3(n, works):
    if n >= sum(works):
        return 0
    works = sorted(works)[::-1]
    flag = 0
    while 1:
        max_num = works[0]
        for i in range(len(works)):
            if works[i]:
                if works[i] == max_num and n > 0:
                    works[i] -= 1
                    n -= 1
                elif works[i] != max_num and n > 0:
                    break
                else:
                    flag = 1
                    break
        if flag:
            break
    answer = sum(w ** 2 for w in works)
    return answer
    # return answer

print(solution3(4, [4, 3, 3]))
print(solution3(1, [2, 1, 2]))
print(solution3(3, [1, 1]))
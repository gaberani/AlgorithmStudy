# 블록의 번호가 n 일 때, 가장 처음 블록은 n * 2번째 위치에 설치
# 그다음은 n * 3, 그다음은 n * 4, ...로 진행

# 예를 들어 1번 블록은 2,3,4,5, ... 인 위치에 우선 설치합니다.
# 그다음 2번 블록은 4,6,8,10, ... 인 위치에 설치하고,
# 3번 블록은 6,9,12... 인 위치에 설치합니다.
# 이렇게 3번 블록까지 설치하고 나면
# 첫 10개의 블록은 0, 1, 1, 2, 1, 3, 1, 2, 3, 2이됩니다.
#
# 그렙시는 길이가 1,000,000,000인 도로에
# 1번 블록부터 시작하여 10,000,000번 블록까지 규칙대로  놓았습니다.
# 그렙시의 시장님은 특정 구간의 어떤 블록이 깔려 있는지 알고 싶습니다.

# begin, end 는 1 이상 1,000,000,000이하의 자연수 이고, begin는 항상 end보다 작습니다.
# end - begin 의 값은 항상 10,000을 넘지 않습니다.

import math
def solution(begin, end):
    # 구간을 나타내는 두 수 begin, end 가 매개변수
    # 그 구간에 깔려 있는 블록의 숫자 배열(리스트)을 return
    answer = []
    for i in range(begin, end+1):
        if i < 2:
            answer.append(0)
            continue
        for ni in range(2, int(math.sqrt(i))+2):

            if i // ni > 10000000: continue

            # 만약 기존에 블록이 깔려있는 자리라면 그 블록을 새로운 블록으로
            if i % ni == 0:
                answer.append(i // ni)
                break
        # 소수라면 1밖에 못들어감
        else:
            answer.append(1)
    return answer


print(solution(1, 10))
# [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]
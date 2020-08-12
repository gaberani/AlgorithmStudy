def solution(skill, skill_trees):
    # skill: 선행 스킬 순서
    # 스킬은 중복해 주어지지 않습니다.
    # skill_trees: 유저들이 만든 스킬트리1를 담은 배열
    # 스킬트리 내 스킬이 중복해 주어지지 않습니다.
    answer = 0
    for skill_tree in skill_trees:
        idx = 0
        flag = 0
        for s in skill_tree:
            # print(s, skill_tree[idx])
            if s in skill:
                if s == skill[idx]:
                    idx += 1
                else:
                    flag = 1
                    break
            if idx == len(skill)-1:
                break
        if not flag:
            answer += 1
        # print(answer)
    return answer


# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "AEFG"]))
print(solution("CBD", ["BDF", "CEFD"]))

# 은근 쉬운데 통과 안되시는분들 아래사항 체크 :
#
# 선행 CBD 를 예로 :
# CXF : 선행중 C만 찍는 경우 -> 가능
# ASF : 선행중 아무것도 찍지 않는 경우 -> 가능 (여기서 많이 틀리시는듯)
#
# BDF : 선행중 C가 없는데 뒤로는 찍은경우 -> 불가능
# CEFD : 선행중 B 이후로 찍지 못하는데 찍는경우 -> 불가능
# (불가능 예제 두개는 결국 안찍은 스킬 뒤로 찍은게 나오면 안된다는 얘기)
#
# 이 외 나머지는 찍은 순서만 체크하시면 됩니다.
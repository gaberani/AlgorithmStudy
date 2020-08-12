def solution(skill, skill_trees):
    answer = 0
    # 각 선행 스킬에 번호 1번부터 부여
    skill_dict = {skill[i]:i+1 for i in range(len(skill))}
    for s in skill_trees:
        # 스킬트리 속 선행 스킬에 해당하는 번호를 담는 stack
        stack = [0]
        for a in s:
            # 선행스킬에 속하는 스킬이면
            if a in skill_dict:
                # 바로 전 스킬 순서보다 1 커야 순서대로 진행 가능
                if stack[-1]+1==skill_dict[a]:
                    stack.append(skill_dict[a])
                else:
                    break
        else:
            answer += 1
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
# result = 2

print(solution(skill, skill_trees))
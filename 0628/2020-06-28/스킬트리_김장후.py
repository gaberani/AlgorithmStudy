def solution(skills, skill_trees):
    answer = 0
    for tree in skill_trees:
        flag = 0
        idx = 0
        for skill in skills:
            while idx < len(tree):
                tmp = tree[idx]
                if tmp not in skills:
                    idx += 1
                elif tmp in skills and tmp == skill:
                    idx += 1
                    break
                else:
                    flag = 1
                    break
            if flag:
                break
        if not flag:
            answer += 1
    return answer


skills = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skills, skill_trees))
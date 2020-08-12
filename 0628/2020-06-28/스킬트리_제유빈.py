def solution(skill, skill_trees):
    ans = 0
    for tree in skill_trees:  # 스킬트리 
        temp = []             # 스킬 문자열 저장 => (인덱스, 값)
        for i in range(len(skill)):
            if skill[i] in tree:
                temp.append([tree.index(skill[i]), skill[i]])
        # 비교
        comp = list(zip([x[1] for x in sorted(temp, key=lambda x: x[0])], skill))
        for x in comp:
            if x[0] != x[1]: break
        else: ans += 1
    return ans

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2
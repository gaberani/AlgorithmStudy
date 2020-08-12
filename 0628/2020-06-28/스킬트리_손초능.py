def solution(skill, skill_trees):
    skill = {skill[i-1]: i for i in range(1, len(skill)+1)}
    n = len(skill_trees)
    answer = 0
    for i in range(n):
        m_idx = 0
        for j in range(len(skill_trees[i])):
            idx = skill.get(skill_trees[i][j], 0)
            if idx==0: continue
            else:
                if idx != m_idx+1: break
                m_idx = idx
        else: answer += 1
    return answer
def solution(N, stages):
    answer = list(range(1, N+1))
    people = [0]*(N+1)
    fail = [0]*(N+1)
    # 스테이지별 통과한 사람, 실패한 사람 정리
    for stage in stages:
        for s in range(stage):  # 통과한 사람
            people[s] += 1
        fail[stage-1] += 1      # 통과하지 못한 사람
    # 실패율 계산
    F = [0]*(N)
    for n in range(N):
        if people[n]:
            F[n] = fail[n]/people[n]
    for i in range(N-1):
        for j in range(i, N):
            if F[i] < F[j]:
                F[i], F[j] = F[j], F[i]
                answer[i], answer[j] = answer[j], answer[i]
            elif F[i] == F[j] and answer[i] > answer[j]:
                answer[i], answer[j] = answer[j], answer[i]
    return answer
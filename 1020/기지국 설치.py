# N개의 아파트가 일렬로 쭉 늘어서 있습니다.
# 4g 기지국을 5g 기지국으로 바꾸려 합니다.
# 5g 기지국은 4g 기지국보다 전달 범위가 좁아

# 아파트의 개수 N
# 현재 기지국이 설치된 아파트의 번호가 담긴 1차원 배열 stations
# 전파의 도달 거리 W


# station 기준 풀이
def solution(N, stations, W):
    answer = 0
    apart = []
    start = 1
    for station in stations:
        end = station-W-1
        if start <= end:
            apart.append([start, end])
        start = station+W+1
    if start <= N:
        apart.append([start, N])

    for start, end in apart:
        print(start, end)
        tmp = (end-start+1) // (2*W+1)
        flag = (end-start+1) % (2*W+1)
        answer += tmp
        if flag:
            answer += 1
    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
print(solution(16, [], 2))

# 집의 개수가 N일때
# 선형복잡도 O(N)을 가지면 효율성 테스트를 통과하지 못하고,
# station의 개수가 T라면 O(T)로 문제를 풀어내야 합니다.
# 집 기준 풀이
def solution1(N, stations, W):
    answer = 0
    apart = [0]*N
    for s in stations:
        for i in range(s-W-1, s+W):
            if 0 <= i < N:
                apart[i] = 1

    cnt = 0
    for i in range(N):
        if apart[i] == 0:
            if cnt == W*2+1:
                cnt = 0
                answer += 1
            cnt += 1
        elif apart[i] == 1:
            if cnt:
                cnt = 0
                answer += 1
    if cnt:
        answer += 1
    return answer
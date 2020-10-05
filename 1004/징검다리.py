
# 출발지점부터 도착지점까지의 거리 distance,
# 바위들이 있는 위치를 담은 배열 rocks,
# 제거할 바위의 수 n
def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks = sorted(rocks)
    rocks.append(distance)
    rnum = len(rocks)

    while start <= end:
        remove = 0
        pre = 0
        min_inter = 10000000001
        mid = (start + end) // 2

        for i in range(rnum):
            if rocks[i] - pre < mid:  # rocks[i]-prev가 inter값
                remove += 1  # 바위제거

            else:  # 바위 제거 안할경우
                min_inter = min(min_inter, rocks[i] - pre)
                pre = rocks[i]  # 현재 바위위치를 pre로

        if remove > n:
            end = mid - 1
        else:
            answer = min_inter
            start = mid + 1

    return answer

N = int(input())
# 계단수 끝자리를 인덱스로 갖는 cnt 배열(개수 저장)
cnt = [1]*10
# 0으로 시작하는 수는 없다.
cnt[0] = 0
for _ in range(N-1):
    # 다음 계단수 정보 저장
    tmp = [0]*10
    for i in range(9):
        # 전 계단수 끝자리보다 1 큰 수를 끝자리로 갖는 계단수
        tmp[i+1] += cnt[i]
        # 전 계단수 끝자리보다 1 작은 수를 끝자리로 갖는 계단수
        tmp[i] += cnt[i+1]
    # cnt 갱신
    cnt = tmp
print(sum(cnt)%1000000000)
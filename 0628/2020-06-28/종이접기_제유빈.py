def solution(n):
    ans = [0]
    # n == 1인 경우 그냥 return
    if n > 1:
        # 접기
        for _ in range(n-1):
            # 새로 추가될 숫자 개수
            new = len(ans)
            # 임시 저장할 리스트
            temp = [0]*new
            for j in range(new):
                # 역순으로 저장
                # 이전에 저장된 값이 1이면 0, 0이면 1 저장
                temp[new-j-1] = ans[j] ^ 1
            # 리스트에 추가
            ans += [0]+temp
    return ans

print(solution(1)) # [0]
print(solution(2)) # [0, 0, 1]
print(solution(3)) # [0, 0, 1, 0, 0, 1, 1]
print(solution(4))
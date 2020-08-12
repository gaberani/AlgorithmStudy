N = int(input())
num_lst = list(map(int ,input().split()))
oper_lst = list(map(int, input().split()))
# 연산자 순서: +, -, *, /

def dfs(idx, result, visit):
    global minV, maxV
    if idx == N:
        # print(result)
        if minV > result:
            minV = result
        if maxV < result:
            maxV = result
    else:
        if visit[0] < oper_lst[0]:
            tmp = result + num_lst[idx]
            visit[0] += 1
            dfs(idx+1, tmp, visit)
            visit[0] -= 1
        if visit[1] < oper_lst[1]:
            tmp = result - num_lst[idx]
            visit[1] += 1
            dfs(idx+1, tmp, visit)
            visit[1] -= 1
        if visit[2] < oper_lst[2]:
            tmp = result * num_lst[idx]
            visit[2] += 1
            dfs(idx+1, tmp, visit)
            visit[2] -= 1
        if visit[3] < oper_lst[3]:
            # 부호가 다르고
            if result * num_lst[idx] < 0:
                # 값의 크기가 다르면
                if abs(result) != abs(num_lst[idx]) and abs(result)/abs(num_lst[idx]) != abs(result)//abs(num_lst[idx]):
                    tmp = (result//num_lst[idx]) + 1
                # 값의 크기 같으면
                else:
                    tmp = (result//num_lst[idx])
            else:
                tmp = result//num_lst[idx]
            visit[3] += 1
            dfs(idx+1, tmp, visit)
            visit[3] -= 1

minV, maxV = 2**63-1, -(2**63-1)
dfs(1, num_lst[0], [0, 0, 0, 0])
# 첫째 줄: 만들 수 있는 식의 결과의 최댓값, 둘째 줄: 최솟값
print(maxV)
print(minV)
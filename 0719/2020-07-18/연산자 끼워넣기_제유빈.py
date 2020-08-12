import sys

# 연산자 배열 순열 - 중복된 원소가 있는 순열
def permu(i, n, op, V):
    if i == n:
        operators.append(op[:])
        pass
    else:
        for k in range(n):
            if not V[k] and (k == 0 or operator[k-1] != operator[k] or V[k-1]):
                V[k], op[i] = 1, operator[k]
                permu(i+1, n, op, V)
                op[i], V[k] = 0, 0

N = int(sys.stdin.readline())
# 숫자 배열
A = list(map(int, sys.stdin.readline().split()))
# 각 연산자의 개수가 주어진 리스트
tmp = list(map(int, sys.stdin.readline().split()))

# 연산자를 숫자로 변환하여 저장 - 0: +, 1: -, 2: *, 3: /
operator = []
for i in range(4):
    for _ in range(tmp[i]):
        operator.append(i)

# 연산자 배열 순열
operators = []
permu(0, N-1, [0]*(N-1), [0]*(N-1))


min_val, max_val = 10**9, -10**9
# 모든 가능한 연산자 순서에 대해 최댓값, 최솟값 찾기
for op in operators:
    val = A[0]
    for j in range(N-1):
        if op[j] == 0:
            val += A[j+1]
        elif op[j] == 1:
            val -= A[j+1]
        elif op[j] == 2:
            val *= A[j+1]
        else:
            if val >= 0:
                val //= A[j+1]
            else:
                val = -(a신bs(val)//A[j+1])
    # 최댓값, 최솟값 갱
    if val > max_val: max_val = val
    if val < min_val: min_val = val
print(max_val)
print(min_val)

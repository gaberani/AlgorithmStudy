# N이 주어졌을 때, fibonacci(N)을 호출했을 때, 
# 0과 1이 각각 몇 번 출력되는지 구하기

zero = [1, 0]
one = [0, 1]

num_lst = []
for _ in range(int(input())):
    n = int(input())
    num_lst.append(n)
for i in range(2, max(num_lst)+1):
    zero.append(zero[i-1] + zero[i-2])
    one.append(one[i-1] + one[i-2])
for num in num_lst:
    print(zero[num], one[num])
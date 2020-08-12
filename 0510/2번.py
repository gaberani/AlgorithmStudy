# 만약 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출
# 제출한 숫자가 가장 큰 참가자를 우승자로 선정하며,
# 우승자가 제출한 숫자를 우승상금으로 지급
import copy
def calc(num1, num2, oper):
    if oper == '*':
        return num1*num2
    elif oper == '-':
        return num1-num2
    else:
        return num1+num2

def solution(expression):
    answer = 0
    operation = ['*', '-', '+']
    all_operation_order = [['*','-','+'], ['*','+','-'], ['+','*','-'], ['+','-','*'], ['-','*','+'], ['-','+','*']]
    num_lst = []
    pre_e = 0
    # 입력 정리
    for e in range(len(expression)):
        if expression[e] in operation:
            num_lst.append(int(expression[pre_e:e]))
            num_lst.append(expression[e])
            pre_e = e+1
    num_lst.append(int(expression[pre_e:]))
    # order대로 풀어서 가장 큰 값 찾기
    for order in all_operation_order:
        tmp_lst = copy.deepcopy(num_lst)
        print(order, tmp_lst)
        for o in order:  # 연산자 순서가 곧 우선 순위
            tmp = []
            flag = 0
            for idx in range(len(tmp_lst)):
                if flag:
                    flag = 0
                else:
                    if tmp_lst[idx] == o:
                        pre_info = tmp.pop()
                        tmp.append(calc(pre_info, tmp_lst[idx+1], o))
                        flag = 1
                    else:
                        tmp.append(tmp_lst[idx])
            tmp_lst = tmp
        if answer < abs(tmp_lst[0]):
            answer = abs(tmp_lst[0])
    return answer

print(solution("100-200*300-500+20"	))
print(solution("50*6-3*2"	))
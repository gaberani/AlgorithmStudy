def solution(n):
    answer = []
    i = 0
    ni = (3**i)*3
    while n >= ni:
        i += 1
        ni += (3**i)*3
    print(i)

    for x in range(i, -1, -1):
        for a in range(3):
            if n >= (3**x)*a:
                na = a
        n -= (3**x)*na
        answer.append((3**x)*na)
    if n != 0:
        answer.append(n)

    # if n % 3 == 1:
    #     answer += '1'
    # elif n % 3 == 2:
    #     answer += '2'
    # elif n % 3 == 3:
    #     answer += '4'

    return answer

print(solution(21))
# 10진법	124 나라	10진법	124 나라
# 1	        1	        6	    14
# 2	        2	        7	    21
# 3	        4	        8	    22
# 4	        11	        9	    24
# 5	        12	        10	    41
#                       11      42
#                       12      44
#                       13:111  14:112  15:114  16:121  17:122  18:124  19:141  20:142  21:144  22:211
# [27*3] [9*3], [3*3], [1*3]
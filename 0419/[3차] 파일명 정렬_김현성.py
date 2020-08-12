def solution(files):
    answer = []
    num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for file in files:
        flag, idx = 0, 0
        head, number, tail = '', '', ''
        for i in range(len(file)):
            # 숫자를 만날때 까지
            if flag == 0 and file[i] in num_lst:
                head = file[:i]
                idx = i
                flag = 1
            elif flag == 1 and file[i] not in num_lst:
                number, tail = file[idx:i], file[i:]
                flag = -1
            if flag == 1 and i == len(file)-1:
                number = file[idx:]
                print('hi')
        answer.append([head, number, tail])
    print(answer)
    answer = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    for a in range(len(answer)):
        answer[a] = answer[a][0] + answer[a][1] + answer[a][2]
    return answer

# 출력: [img1.png, IMG01.GIF, img02.png, img2.JPG, img10.png, img12.png]
# print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
print(solution(['F-5', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))
print(solution(['F-5']))
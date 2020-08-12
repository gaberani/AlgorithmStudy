from copy import deepcopy
def solution(word, pages):
    answer = 0
    # 소문자로 통일
    score = dict()          # 기본 점수
    link_score = dict()     # 자신의 외부 링크수
    linked_score = dict()   # 링크된 수
    word = word.lower()
    for page in range(len(pages)):
        pages[page] = pages[page].lower()
        flag = 0        # 자신의 링크와 외부 링크 구분 (생략가능할듯)
        score_cnt = 0   # 검색어 점수 count
        tmp_lst = []    # 자신의 외부링크 모으는 리스트
        for p in range(len(pages[page])):
            # 검색어 점수 세기
            if pages[page][p] == word[0]:
                # 검색어도 일치하고 앞 뒤로 알파벳 체크 둘다 False 점수 += 1
                if pages[page][p:p+len(word)] == word and pages[page][p-1].isalpha() == 0 and pages[page][p+len(word)].isalpha() == 0:
                    score_cnt += 1
            # 링크, 외부 링크 점수 세기
            if pages[page][p] == 'h':
                # 자기 링크 이름 찾기 ="https://
                if flag == 0 and pages[page][p-9:p+8] == 'content="https://':
                    idx = p
                    while pages[page][idx] != '"':
                        idx += 1
                    tmp = pages[page][p:idx]
                    flag = 1
                # 외부 링크 찾기<a href=
                elif pages[page][p-3:p+5] == '<a href=' and flag == 1:
                    idx = p+6
                    while pages[page][idx] != '"':
                        idx += 1
                    tmp_lst.append(pages[page][p+6:idx])
        link_score[tmp] = tmp_lst
        score[tmp] = score_cnt
    result = deepcopy(score)
    for key, values in link_score.items():
        # print(key, values)
        for value in values:
            try:
                result[value] += score.get(key)/len(values)
            except:
                pass
    max_val, idx_cnt = 0, 0
    for key, value in result.items():
        if max_val < value:
            answer = idx_cnt
            max_val = value
        idx_cnt += 1
    return answer

# print(solution('Blind', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\"><head>  <meta charset=\"utf-8\">  <meta property=\"og:url\" content=\"https://a.com\"/></head>  <body>Blind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. <a href=\"https://b.com\"> Link to b </a></body></html>",
#                          "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\"><head><meta charset=\"utf-8\"><meta property=\"og:url\" content=\"https://b.com\"/></head><body>Suspendisse potenti. Vivamus venenatis tellus non turpis bibendum, <a href=\"https://a.com\"> Link to a </a>blind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.<a href=\"https://c.com\"> Link to c </a></body></html>",
#                          "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\"><head>  <meta charset=\"utf-8\">  <meta property=\"og:url\" content=\"https://c.com\"/></head> <body>Ut condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind<a href=\"https://a.com\"> Link to a </a></body></html>"
#                          ]))

print(solution('Muzi', ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))
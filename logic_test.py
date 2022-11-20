def fixed_score(score_list):
    '''
    國泰補習班中，有五位學生期中考的成績分別為[53, 64, 75, 19, 92]，
    但是老師在輸入成績的時候看反了，把五位學生的成績改成了[35, 46, 57, 91, 29]，
    請用一個函數來將學生的成績修正。

    輸入: [35, 46, 57, 91, 29]
    輸出: [53, 64, 75, 19, 92]
    '''
    fixed_list = []
    for i in score_list:
        score_res = str(i)
        fixed_list.append(int(score_res[::-1]))
    print(fixed_list)
    return fixed_list


def count_words(input_text):
    '''
    國泰銀行要慶祝六十周年，需要買字母貼紙來布置活動空間，文字為"Hello welcome to Cathay 60th year anniversary"，
    請寫一個程式計算每個字母(大小寫視為同個字母)出現次數
    輸出：
    0 1
    6 1
    A 4
    C 2
    E 5
    H 3
    ....(繼續印下去)
    '''
    count_dic = {}
    clear_list = []
    upper_text = [i.upper() for i in input_text]

    for i in upper_text:
        # print(ord(i),i)
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1
    for k, _ in count_dic.items():
        if k != ' ':
            clear_list.append(k)
    clear_list = sorted(clear_list)
    for i in clear_list:
        print(i, count_dic[i])


def team_game(n):
    '''
    QA部門今天舉辦團康活動，有n個人圍成一圈，順序排號。從第一個人開始報數（從1到3報數），凡報到3的人退出圈子。
    請利用一段程式計算出，最後留下的那位同事，是所有同事裡面的第幾順位?
    :return:
    '''
    if n == 0:
        print('n 為 0 請重新輸入')
        return False
    answer = []
    people_list = [i for i in range(1, n + 1)]
    x = 0
    temp = people_list
    for ii in range(n):
        # print(temp)
        for i in temp:
            x += 1
            if x % 3 != 0:
                answer.append(i)
            else:
                # print(f'數到三:{i}')
                pass
        temp = answer
        answer = []
        if len(temp) == 1:
            break

    print(f"第{temp}順位")


fixed_score(score_list=[35, 46, 57, 91, 29])
count_words(input_text="Hello welcome to Cathay 60th year anniversary")
team_game(n=100)

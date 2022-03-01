def solution(lottos, win_nums):
    cnt = 0
    cnt_zero = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        elif i == 0:
            cnt_zero += 1
        else:
            continue
    dic_answer = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    return [dic_answer[cnt+cnt_zero], dic_answer[cnt]]
# BOJ 1018 체스판다시칠하기
# 브루트포스



import sys

n, m = map(int, sys.stdin.readline().split())

# 맨왼쪽위 검은색 or 흰색 8x8 체스판 두개 생성
wb = list('WB' * 4)
bw = list('BW' * 4)
w_top = [wb,bw]*4
b_top = [bw,wb]*4

# 보드판 입력
board_list = []
for i in range(n):
    row = list(sys.stdin.readline().rstrip())
    board_list.append(row)

wb_cnt = 100
bw_cnt = 100
# 8X8로 보드 잘라가며 비교
for row in range(n-7):
    board_cut = board_list[row:row+8]
    for col in range(m-7):
        wb_tmp = 0
        bw_tmp = 0
        for i in range(8):
            for j in range(8):
                if board_cut[i][col:col+8][j] != w_top[i][j]:
                    wb_tmp += 1
                if board_cut[i][col:col+8][j] != b_top[i][j]:
                    bw_tmp += 1
        if wb_cnt > wb_tmp:
            wb_cnt = wb_tmp
        if bw_cnt > bw_tmp:
            bw_cnt = bw_tmp

print(min(wb_cnt, bw_cnt))








# import numpy as np

############### np 사용 XXXXXXXXXXXXXXX #################
# n, m = map(int, sys.stdin.readline().split())
# wb = list('WB' * 4)
# bw = list('BW' * 4)
# w_top = np.array([wb,bw]*4)
# b_top = np.array([bw,wb]*4)


# # NxM 보드 입력받기
# # 0행렬 만든 후 concatenate
# arr_empty = np.zeros(m).reshape(1,-1)
# for i in range(n):
#     row = np.array(list(sys.stdin.readline().rstrip())).reshape(1,-1)
    
# # 0행렬 삭제
# arr_full = np.delete(arr_empty, 0, axis=0)

# # 보드를 8x8 로 잘라가며 만들어 놓은 8x8 체스판과 비교, 
# wb_cnt = 100
# bw_cnt = 100
# for row in range(n-7):
#     for col in range(m-7):
#         arr_cut = arr_full[row:row+8, col:col+8]
#         if wb_cnt > (arr_cut!=w_top).sum():
#             wb_cnt = (arr_cut != w_top).sum()
#         if bw_cnt > (arr_cut!=b_top).sum():
#             bw_cnt = (arr_cut != b_top).sum()
# print(min(wb_cnt, bw_cnt))

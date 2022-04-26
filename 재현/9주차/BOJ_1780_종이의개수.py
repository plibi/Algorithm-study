# 아이디어 : graph의 element가 모두 같은지 확인 같으면 element 개수만큼 +, 다르면 divide
# => 시간초과, 모두 같은지 확인하는 과정이 반복되면서 시간초과 발생하는 듯 하여
# => 다음 element와 비교해서 다르면 바로 divide하는 방식으로 변경

import sys
input = sys.stdin.readline

# 1 3 9 27 81 243 729 2187
n = int(input())
paper = []
nums = [0, 0, 0]    # -1, 0, 1

for _ in range(n):
    line = list(map(int, input().split()))
    paper.append(line)
print(paper)

# # graph가 모두 같은 수인지 확인하는 함수
# def same(graph):
#     first = graph[0][0]
#     for i in range(len(graph)):
#         for j in range(len(graph[0])):
#             if first != graph[i][j]:
#                 return False
#     return True

# # graph를 9등분 하는 함수
# def divide(graph):
#     print(graph)
#     if len(graph) == 1:
#         print('Yes!')
#         nums[graph[0][0]+1] += 1
#     else:
#         print('No!')
#         if same(graph):
#             print('Same')
#             nums[graph[0][0]+1] += 1
#         else:
#             print('Not same')
#             division = len(graph) // 3
#             part1 = [0, 1, 2]
#             part2 = [0, 1, 2]
#             for i in part1:
#                 for j in part2:
#                     temp = []
#                     for row in range(division*i, division*(i+1)):
#                         temp_col = []
#                         for col in range(division*j, division*(j+1)):
#                             temp_col.append(graph[row][col])
#                         print(temp_col)
#                         temp.append(temp_col)
#                     divide(temp)

def cut(x, y, n):
    check = paper[x][y]
    for r in range(x, x+n):
        for c in range(y, y+n):
            if check != paper[r][c]:
                div = n // 3
                # 1, 2, 3
                cut(x, y, div)
                cut(x, y + div, div)
                cut(x, y + div*2, div)
                # 4, 5, 6
                cut(x + div, y, div)
                cut(x + div, y + div, div)
                cut(x + div, y + div*2, div)
                # 7, 8, 9
                cut(x + div*2, y, div)
                cut(x + div*2, y + div, div)
                cut(x + div*2, y + div*2, div)
                return

    if check == -1:
        nums[0] += 1
    elif check == 0:
        nums[1] += 1
    else:
        nums[2] += 1

# divide(paper)
cut(0, 0, n)
for number in nums:
    print(number)
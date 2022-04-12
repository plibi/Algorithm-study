# 소요시간 : 30분
# 아이디어 : 

import sys
input = sys.stdin.readline

# 1 3 9 27 81 243 729 2187
n = int(input())
paper = []
nums = [0, 0, 0]    # -1, 0, 1

for _ in range(n):
    line = list(map(int, input().split()))
    paper.append(line)

# graph가 모두 같은 수인지 확인하는 함수
def same(graph):
    first = graph[0][0]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if first != graph[i][j]:
                return False
    return True

# graph를 9등분 하는 함수
def divide(graph):
    if len(graph) == 1:
        nums[graph[0][0]+1] += 1
    else:
        for i in range(division):
            for j in range(division):
                ...

        g1, g2, g3 = [], [], []
        g4, g5, g6 = [], [], []
        g7, g8, g9 = [], [], []
        division = len(graph)//3

        for r1 in range(division):
            line1 = []
            line2 = []
            line3 = []
            for c1 in range(division):
                line1.append(graph[r1][c1])
            g1.append(line1)
            for c2 in range(division, 2*division):
                line2.append(graph[r1][c2])
            g2.append(line2)
            for c3 in range(2*division, 3*division):
                line3.append(graph[r1][c3])
            g3.append(line3)
        
        if same(g1) == True:
            nums[g1[0][0]+1] += 1
        else:
            divide(g1)
        if same(g2) == True:
            nums[g2[0][0]+1] += 1
        else:
            divide(g2)
        if same(g3) == True:
            nums[g3[0][0]+1] += 1
        else:
            divide(g3)    

        for r2 in range(division, 2*division):
            line1 = []
            line2 = []
            line3 = []
            for c1 in range(division):
                line1.append(graph[r2][c1])
            g4.append(line1)
            for c2 in range(division, 2*division):
                line2.append(graph[r2][c2])
            g5.append(line2)
            for c3 in range(2*division, 3*division):
                line3.append(graph[r2][c3])
            g6.append(line3)
        # print('g1:', g1, 'g2:',g2, 'g3:',g3)
        if same(g4) == True:
            nums[g4[0][0]+1] += 1
        else:
            divide(g4)
        if same(g5) == True:
            nums[g5[0][0]+1] += 1
        else:
            divide(g5)
        if same(g6) == True:
            nums[g6[0][0]+1] += 1
        else:
            divide(g6)

        for r3 in range(2*division, 3*division):
            line1 = []
            line2 = []
            line3 = []
            for c1 in range(division):
                line1.append(graph[r3][c1])
            g7.append(line1)
            for c2 in range(division, 2*division):
                line2.append(graph[r3][c2])
            g8.append(line2)
            for c3 in range(2*division, 3*division):
                line3.append(graph[r3][c3])
            g9.append(line3)
        
        if same(g7) == True:
            nums[g7[0][0]+1] += 1
        else:
            divide(g7)
        if same(g8) == True:
            nums[g8[0][0]+1] += 1
        else:
            divide(g8)
        if same(g9) == True:
            nums[g9[0][0]+1] += 1
        else:
            divide(g9)
                


# 모두 같은 수인가 확인, 아니면 9등분
# check = same(paper)
# if check == True:
#     nums[paper[0][0]+1] += 1
# else:
#     ...
divide(paper)
for number in nums:
    print(number)
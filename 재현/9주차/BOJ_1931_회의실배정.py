# 소요시간: 20분
# 아이디어: 회의시간 x(시작), y(종료)를 (x, y) 형식으로 입력받아 y순 다음 x순으로 정렬
# 결과적으로 가장 빨리 끝나고(y), 가장 일찍 시작 하는(x) 순서를 얻을 수 있다 

import sys
input = sys.stdin.readline
N = int(input())
nums = [tuple(map(int, input().split())) for _ in range(N)]
nums.sort(key=lambda x: (x[1], x[0]))
# print(nums)

count = 1
end = nums[0][1]
for i in range(1, N):
    if nums[i][0] >= end:
        end = nums[i][1]
        count += 1
print(count)

# 정렬 결과
# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
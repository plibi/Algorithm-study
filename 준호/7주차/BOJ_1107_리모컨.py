import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
but_list = list(map(int, sys.stdin.readline().split()))

answer = 999999

for i in range(1000001):
    tmp = True
    num_list = list(map(int, str(i)))
    for j in num_list:
        if j in but_list:
            tmp = False
    if tmp == True:
        answer = min(answer, len(str(i))+abs(i-n))

answer = min(answer, abs(100-n))
print(answer)
    











# n1 = n
# cnt = 0
# while True:
#     tmp = list(map(int, list(str(n1))))
#     tmp_n = 0
#     for i in tmp:
#         if i in but_list:
#             break
#         else:
#             tmp_n += 1
#     if tmp_n == len(tmp):
#         break
#     n1 += 1
#     cnt += 1
#     if cnt > 10**len(tmp):
#         break

# answer = cnt+len(tmp)


# n2 = n
# cnt_2=0
# while True:
#     tmp = list(map(int, list(str(n2))))
#     tmp_n = 0
#     for i in tmp:
#         if i in but_list:
#             break
#         else:
#             tmp_n += 1
#     if tmp_n == len(tmp):
#         break
#     n2 -= 1
#     cnt_2 += 1
#     if cnt_2 > 10**len(tmp):
#         break

# answer_2 = cnt_2+len(tmp)



# if n == 100:
#     print(0)
# else:
#     print(min(answer, answer_2))


# '-'를 기준으로 split으로 나눠주고 나눈 부분들을 다 더해주는 아이디어 사용

N = input()
temp = N.split('-')
t = []
for i in temp:
    t.append(sum(list(map(int,i.split('+')))))

answer = t[0]
for i in t[1:]:
    answer -= i
print(answer)
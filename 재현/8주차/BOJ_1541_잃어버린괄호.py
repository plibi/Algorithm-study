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

# ex) 55-50+40
# '-'기준으로 split => temp = ['55', '50+40']
# temp[i]를 정리 => t = [55, 90] 
# answer = t[0]로 두고 answer에서 t[1:]들을 전부 빼주면 ok
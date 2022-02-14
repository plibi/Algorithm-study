# 유용한 라이브러리 및 함수들


# eval()
result = eval('(3+5)*7')
print(result)

# sorted() with key
ls = [('한국', 35), ('미국', 90), ('일본', 70), ('중국', 20), ('한국', 40)]
result1 = sorted(ls, key=lambda x:(x[0], x[1]))
result2 = sorted(ls, key=lambda x:(x[0], -x[1]))    # x[0]으로 정렬 같으면 x[1]내림차순
result3 = sorted(ls, key=lambda x:(-x[1]))

print(result1, result2, result3, sep='\n')


# itertools : permutation, combination, 중복순열, 중복조합
from itertools import combinations, permutations
data = ['A', 'B', 'C', 'D']

print(list(permutations(data, 3)))
print(list(combinations(data, 3)))


# Counter
from collections import Counter
data = ['r', 'b', 'r', 'g', 'b', 'b']
counter = Counter(data)                 # iterable을 counter obj로 만듦

print(counter['b'], counter['r'])
print(dict(counter))                    # dict으로 반환

# Collections : deque(덱)
# heapq : heap
# bisect : binary search 기능

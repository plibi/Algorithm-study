from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    doc = deque([(i, int(p)) for i, p in enumerate(list(input().split()))])
    i = 0
    while doc:
        if doc[0] == max(doc, key=lambda x: x[1]):
            if doc[0][0] == M:
                print(i+1)
                break
            else:
                i += 1
                doc.popleft()
        else:
            doc.rotate(-1)
            

# 다른풀이 (list만 사용)
# https://www.acmicpc.net/source/14968208
import sys

class stack:
    def __init__(self, arr = []):
        self.arr = arr
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def push(self, item):
        self.arr.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.arr.pop()
        else:
            return False
        
    def size(self):
        return len(self.arr)

    def top(self):
        if not self.isEmpty():
            return self.arr[-1]
        else:
            return False
    
    def isIn(self, item):
        return item in self.arr

num = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(num)]

st = stack()
result = []
cnt = 1
pos = True

for i in arr:
    while cnt <= i:
        st.push(cnt)
        result.append('+')
        cnt += 1
    
    if st.top() == i:
        st.pop()
        result.append('-')
    else:
        pos = False

if pos:
    print(*result, sep = '\n')
else:
    print('NO')
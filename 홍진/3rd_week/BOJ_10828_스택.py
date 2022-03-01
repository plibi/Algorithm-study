import sys

class stack:
    def __init__(self):
        self.arr = []
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def push(self, item):
        self.arr.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.arr.pop()
        else:
            return -1
        
    def size(self):
        return len(self.arr)
    
    def empty(self):
        return int(self.isEmpty())

    def top(self):
        if not self.isEmpty():
            return self.arr[-1]
        else:
            return -1

result = stack()
for _ in range(int(sys.stdin.readline())):
    inp = sys.stdin.readline().split()
    if inp[0] == 'push':
        result.push(inp[1])
    elif inp[0] == 'pop':
        print(result.pop())
    elif inp[0] == 'size':
        print(result.size())
    elif inp[0] == 'empty':
        print(result.empty())
    elif inp[0] == 'top':
        print(result.top())
import sys

class deque:
    def __init__(self):
        self.arr = []
    
    def isEmpty(self):
        return len(self.arr) == 0
    
    def push_front(self, item):
        self.arr = [item] + self.arr

    def push_back(self, item):
        self.arr.append(item)

    def pop_front(self):
        if not self.isEmpty():
            item = self.arr[0]
            self.arr = self.arr[1:]
            return item
        else:
            return -1
    
    def pop_back(self):
        if not self.isEmpty():
            return self.arr.pop()
        else:
            return -1
    
    def front(self):
        if not self.isEmpty():
            return self.arr[0]
        else:
            return -1

    def back(self):
        if not self.isEmpty():
            return self.arr[-1]
        else:
            return -1

    def size(self):
        return len(self.arr)
    
    def empty(self):
        return int(self.isEmpty())

result = deque()
for _ in range(int(sys.stdin.readline())):
    inp = sys.stdin.readline().split()
    if inp[0] == 'push_front':
        result.push_front(inp[1])
    elif inp[0] == 'push_back':
        result.push_back(inp[1])
    elif inp[0] == 'pop_front':
        print(result.pop_front())
    elif inp[0] == 'pop_back':
        print(result.pop_back())
    elif inp[0] == 'size':
        print(result.size())
    elif inp[0] == 'empty':
        print(result.empty())
    elif inp[0] == 'front':
        print(result.front())
    elif inp[0] == 'back':
        print(result.back())
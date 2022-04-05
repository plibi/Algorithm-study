#
#

import sys
n, r, c = map(int, sys.stdin.readline().split())

count = 0
while n != 0:
    n -= 1
    size = 2**n

    # bottom right
    if r >= size and c >= size:
        count += size*size*3
        r -= size
        c -= size

    # bottom left
    if r >= size and c < size:
        count += size*size*2
        r -= size
    
    # top right
    if r < size and c >= size:
        count += size*size
        c -= size
    # top left
    if r < size and c < size:
        ...
        
print(count)

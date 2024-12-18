import re
from collections import deque

file = open("data18.txt").read().split('\n')
byte_list = [(int(x) for x in re.findall("\d+",line)) for line in file]
dir = [(-1,0),(0,1),(1,0),(0,-1)]

G, FIRST_FALL = 71, 1024
grid = [[0 for _ in range(G)] for _ in range(G)]
i=0

for y, x in byte_list:
    flag = True
    grid[x][y] = '#'
    i+=1

    if i>=FIRST_FALL:
        temp_list = deque([(0,0,0)])
        steps = set()
        while temp_list:
            tot, r, c = temp_list.popleft()
            if (r,c) == (G-1, G-1):
                flag = False
                if i==FIRST_FALL:
                    print(tot)
                break
            if (r,c) in steps:
                continue
            steps.add((r,c))
            for rd, cd in dir:
                rn, cn = r+rd, c+cd
                if 0<=rn<G and 0<=cn<G and grid[rn][cn] != '#':
                    temp_list.append((tot+1, rn, cn))
        if flag:
            print(y,x)
            break

from math import inf
from heapq import heappop, heappush
data = open("data16.txt").read().split('\n')

for r in range(len(data)):
    for c in range(len(data[r])):
        if data[r][c] == 'S':
            sr, sc = r, c
        elif data[r][c] == 'E':
            er, ec = r, c

temp_list, paths = [], []
score_trail_record = {}
heappush(temp_list,(0,sr,sc,0,""))
best = inf
while temp_list:
    tot,r,c,dir,path = heappop(temp_list)
    if tot>best:
        break
    if (r,c,dir) in score_trail_record and score_trail_record[(r,c,dir)] < tot:
        continue
    score_trail_record[(r,c,dir)] = tot
    if r==er and c==ec:
        best = tot
        paths.append(path)
    rd, cd = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}[dir]
    rn, cn = r+rd, c+cd
    if 0<=rn<len(data) and 0<=cn<len(data[0]) and data[rn][cn] != '#':
        heappush(temp_list, (tot+1, rn,cn,dir,path+'S'))
    heappush(temp_list, (tot+1000, r, c, (dir+1)%4,path+'R'))
    heappush(temp_list, (tot+1000, r, c, (dir+3)%4,path+'L'))

tiles = set()
tiles.add((sr,sc))
for path in paths:
    tr, tc, dir = sr, sc, 0
    for move in path:
        rd, cd = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}[dir]
        rn, cn = tr+rd, tc+cd
        if move=='S':
            tr, tc = rn, cn
            tiles.add((tr,tc))
        elif move=='R':
            dir = (dir+1)%4
        elif move=='L':
            dir = (dir+3)%4

print(best)
print(len(tiles))

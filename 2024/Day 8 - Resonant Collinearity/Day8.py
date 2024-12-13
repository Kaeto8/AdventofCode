with open("data8.txt") as file:
    data = file.read().split('\n')

L, M = len(data), len(data[0])
pos={}

for i in range(L):
    for j in range(M):
        if data[i][j] in pos:
            pos[data[i][j]].append((i,j))
        else:
            pos[data[i][j]] = [(i,j)]
pos.pop('.')

set1, set2 = set(), set()
for key,items in pos.items():
    for x1,y1 in items:
        for x2,y2 in items:
            d1, d2 = abs(x2-x1), abs(y2-y1)
            
            if x2>x1 and y2>y1:
                x,y = x1, y1
                if 0<=x-d1<L and 0<=y-d2<M:
                    set1.add((x-d1,y-d2))
                while 0<=x<L and 0<=y<M:
                    set2.add((x,y))
                    x, y = x-d1, y-d2
                x,y = x2, y2
                if 0<=x+d1<L and 0<=y+d2<M:
                    set1.add((x+d1,y+d2))
                while 0<=x<L and 0<=y<M:
                    set2.add((x,y))
                    x, y = x+d1, y+d2

            if x1>x2 and y2>y1:
                x,y = x1, y1
                if 0<=x1+d1<L and 0<=y1-d2<M:
                    set1.add((x+d1,y-d2))
                while 0<=x<L and 0<=y<M:
                    set2.add((x,y))
                    x, y = x+d1, y-d2
                x,y = x2, y2
                if 0<=x-d1<L and 0<=y+d2<M:
                    set1.add((x-d1,y+d2))
                while 0<=x<L and 0<=y<M:
                    set2.add((x,y))
                    x, y = x-d1, y+d2

print(len(set1))
print(len(set2))

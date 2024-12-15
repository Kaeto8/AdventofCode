import re

data = open("data14.txt").read().strip().split('\n')
f = open("test.txt","w")

W,H = 101, 103
arr = [[0 for _ in range(W)] for _ in range(H)]
pos = []

for line in data:
    num = re.findall('-*\d+',line)
    c,r,vh,vv = map(int, num)
    pos.append([c,r,vh,vv])
    arr[r][c] += 1

for i in range(1, 10000):
    Q1, Q2, Q3, Q4 = [],[],[],[]
    for p in pos:
        arr[p[1]][p[0]] -= 1
        newc = (p[0]+p[2])%W
        newr = (p[1]+p[3])%H
        p[0], p[1] = newc, newr
        arr[p[1]][p[0]] += 1

        if p[1]<(H-1)//2 and p[0]<(W-1)//2:
            Q1.append(p)
        elif p[1]>(H-1)//2 and p[0]<(W-1)//2:
            Q2.append(p)
        elif p[1]<(H-1)//2 and p[0]>(W-1)//2:
            Q3.append(p)
        elif p[1]>(H-1)//2 and p[0]>(W-1)//2:
            Q4.append(p)

    if i == 100:
        total = len(Q1)*len(Q2)*len(Q3)*len(Q4)

    for r in range(H):
        for c in range(W):
            if arr[r][c] == 0:
                arr[r][c] = '.'

    f.write(str(i)+"\n")
    for a in arr:
        stri="".join(str(x) for x in a)
        f.write(stri+"\n")
    
    for r in range(H):
        for c in range(W):
            if arr[r][c] == '.':
                arr[r][c] = 0
               
f.close()
print(total)

with open("data12.txt") as file:
    data = file.read().split('\n')

dir = [(0,1),(1,0),(0,-1),(-1,0)]
currentSet = set()
doneSet = set()

def tracer(r, c, plot):
    if (r,c) in currentSet:
        return
    currentSet.add((r,c))
    doneSet.add((r,c))
    for dr, dc in dir:
        newR, newC = r+dr, c+dc
        if  0<=newR<len(data) and 0<=newC<len(data[r]) and plot == data[newR][newC]:
            tracer(newR, newC, plot)

tot, tot2 =0, 0
arrs=[]
for i in range(len(data)):
    for j in range(len(data[i])):
        currentSet.clear()
        if not (i,j) in doneSet:
            arr=[]
            tracer(i, j, data[i][j])
            area = len(currentSet)
            perimeter = 0
            for r, c in currentSet:
                for dr, dc in dir:
                    newR, newC = r+dr, c+dc
                    if 0<=newR<len(data) and 0<=newC<len(data[newR]) and data[newR][newC]!=  data[r][c]:
                        perimeter+=1
                    if newR<0 or newR>=len(data) or newC<0 or newC>=len(data):
                        perimeter+=1
                arr.append((r,c))
            tot += area*perimeter
            arrs.append((area, arr))


for area, y in arrs:
    corner = 0
    for pos in y:
        if not ((pos[0]-1),pos[1]) in y and not (pos[0],(pos[1]-1)) in y:
            corner+=1
        if not ((pos[0]-1),pos[1]) in y and not (pos[0],(pos[1]+1)) in y:
            corner+=1
        if not ((pos[0]+1),pos[1]) in y and not (pos[0],(pos[1]-1)) in y:
            corner+=1
        if not ((pos[0]+1),pos[1]) in y and not (pos[0],(pos[1]+1)) in y:
            corner+=1
        if ((pos[0]-1),pos[1]) in y and (pos[0],(pos[1]-1)) in y and not ((pos[0]-1),(pos[1]-1)) in y:
            corner+=1
        if ((pos[0]-1),pos[1]) in y and (pos[0],(pos[1]+1)) in y and not ((pos[0]-1),(pos[1]+1)) in y:
            corner+=1
        if ((pos[0]+1),pos[1]) in y and (pos[0],(pos[1]-1)) in y and not ((pos[0]+1),(pos[1]-1)) in y:
            corner+=1
        if ((pos[0]+1),pos[1]) in y and (pos[0],(pos[1]+1)) in y and not ((pos[0]+1),(pos[1]+1)) in y:
            corner+=1

    tot2+=area*corner

print(tot)
print(tot2)

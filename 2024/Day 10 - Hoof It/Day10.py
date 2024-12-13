with open("data10.txt") as file:
    data = file.readlines()

arr=[]
for line in data:
    line = line.strip()
    arr.append([int(x) for x in line])

dir = [(0,1),(1,0),(0,-1),(-1,0)]

trails, trails2 = set(), []
def tracer(r, c, num):
    if num == 9:
        trails.add((r,c))
        trails2.append((r,c))
        return
    for dr, dc in dir:
        newR, newC = r+dr, c+dc
        if 0<=newR<len(arr) and 0<=newC<len(arr[0]) and arr[newR][newC] == num+1:
            tracer(newR, newC, num+1)
    return len(trails2), len(trails)

ans, ans2 = 0, 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 0:
            trails.clear()
            trails2.clear()
            ans2 += tracer(i,j,0)[0]
            ans += tracer(i,j,0)[1]

print(ans, ans2)

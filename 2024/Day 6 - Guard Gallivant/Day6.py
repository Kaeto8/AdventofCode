with open('data6.txt') as file:
    data = file.readlines()

i, obstructions = 0, 0
array, pos = [], []

for line in data:
    line=line.strip()
    temp=[]
    for l in range(len(line)):
        temp.append(line[l])
    array.append(temp)

for line in array:
    if '^' in line:
        pos.append(i)
        pos.append(line.index('^'))
    i+=1

for rowWithObstacle in range(len(array)):
    for colWithObstacle in range(len(array[rowWithObstacle])):
        row, col = pos[0], pos[1]
        direction = 0
        places = set()
        placesWithDir = set()
        while True:
            if (row, col, direction) in placesWithDir:
                obstructions += 1 
                break
            placesWithDir.add((row, col, direction))
            places.add((row, col))
            rowUpdate, colUpdate = [(-1,0),(0,1),(1,0),(0,-1)][direction]
            rowNext = row+rowUpdate
            colNext = col+colUpdate
            if not (0<=rowNext<len(array) and 0<=colNext<len(array[rowWithObstacle])):
                break
            if array[rowNext][colNext] == '#' or (rowNext==rowWithObstacle and colNext==colWithObstacle):
                direction = (direction+1)%4
            else:
                row = rowNext
                col = colNext

print(len(places))
print(obstructions)

file = open("data20.txt").read().split('\n')
lines=[line for line in file]
grid = tuple("".join(file))

cheat, cheat2 = 0, 0
MIN, R = 100, len(file)
dirs = [-R, 1, R, -1]
s, e = grid.index("S"), grid.index("E")

distance = {s: 0}
path = [s]
p = s
while p != e:
    for d in dirs:
        if grid[p+d] != "#" and p+d not in distance:
            distance[p+d] = distance[p]+1
            path.append(p+d)
            p += d
for p in path:
    for d in dirs:
        pos1, pos2 = p+d, p+d*2
        if 0<=pos2<len(grid) and grid[pos1] == "#" and grid[pos2] != "#" and distance[pos2] >= distance[p] + 2 + MIN:
            cheat += 1
print(cheat)

probation, success = {}, {}
valid = 0
for p in path[MIN:]:
    man_dist = abs(p%R - s%R) + abs(p//R - s//R)
    if man_dist > 20:
        if man_dist-20 in probation:
            probation[man_dist-20] += [p]
        else:
            probation[man_dist-20] = [p]
    elif (advantage := distance[p] - man_dist - MIN) >= 0:
        if min(20-man_dist, advantage//2)+1 in success:
            success[min(20-man_dist, advantage//2)+1] += [p]
        else:
            success[min(20-man_dist, advantage//2)+1] = [p]
        valid += 1

for p in path[:-MIN]:
    if distance[p] in probation:
        for node in probation[distance[p]]:
            man_dist = abs(p%R - node%R) + abs(p//R - node//R)
            if man_dist > 20:
                if distance[p]+man_dist-20 in probation:
                    probation[distance[p]+man_dist-20] += [node]
                else:
                    probation[distance[p]+man_dist-20] = [node]
            elif (advantage := distance[node] - distance[p] - man_dist - MIN) >= 0: 
                if distance[p]+min(20-man_dist, advantage//2)+1 in success:
                    success[distance[p]+min(20-man_dist, advantage//2)+1] += [node]
                else:
                    success[distance[p]+min(20-man_dist, advantage//2)+1] = [node]
                valid += 1

    if distance[p] in success:
        for node in success[distance[p]]:
            man_dist = abs(p%R - node%R) + abs(p//R - node//R)
            if man_dist > 20:
                if distance[p]+man_dist-20 in probation:
                    probation[distance[p]+man_dist-20] += [node]
                else:
                    probation[distance[p]+man_dist-20] = [node]
                valid -= 1
            elif (advantage := distance[node] - distance[p] - man_dist - MIN) >= 0:
                if distance[p]+min(20-man_dist, advantage//2)+1 in success:
                    success[distance[p]+min(20-man_dist, advantage//2)+1] += [node]
                else:
                    success[distance[p]+min(20-man_dist, advantage//2)+1] = [node]
            else:
                valid-=1


    cheat2 += valid
print(cheat2)

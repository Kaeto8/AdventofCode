data, dir = open("data15.txt").read().strip().split('\n\n')
data = data.split('\n')

def arranger(data, dir, p2):
    data = [[x for x in d] for d in data]
    if p2:
        data2=[]
        for r in range(len(data)):
            row = []
            for c in range(len(data[r])):
                if data[r][c] == '.':
                    row.append('.')
                    row.append('.')
                elif data[r][c] == 'O':
                    row.append('[')
                    row.append(']')
                elif data[r][c] == '#':
                    row.append('#')
                    row.append('#')
                elif data[r][c] == '@':
                    row.append('@')
                    row.append('.')
            data2.append(row)
        data=data2
    i = 0
    for line in data:
        if '@' in line:
            r = i
            c = line.index('@')
            data[r][c] = '.'
        i+=1

    for d in dir:
        if d == '\n':
            continue
        rd,cd = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<': (0,-1)}[d]
        rn, cn = r+rd, c+cd
        if data[rn][cn] == '.':
            r,c = rn,cn
        if data[rn][cn] in '[]O':
            temp_list = [(r,c)]
            checked = set()
            flag = False
            while temp_list:
                ghostr, ghostc = temp_list.pop()
                if (ghostr, ghostc) in checked:
                    continue
                checked.add((ghostr,ghostc))
                if data[ghostr+rd][ghostc+cd] == 'O':
                    temp_list.append((ghostr+rd,ghostc+cd))
                if data[ghostr+rd][ghostc+cd] == '[':
                    temp_list.append((ghostr+rd,ghostc+cd))
                    temp_list.append((ghostr+rd,ghostc+cd+1))
                if data[ghostr+rd][ghostc+cd] == ']':
                    temp_list.append((ghostr+rd,ghostc+cd))
                    temp_list.append((ghostr+rd,ghostc+cd-1))
                if data[ghostr+rd][ghostc+cd] == '#':
                    flag = True
                    break
            if flag == False:
                while checked:
                    for ghostr, ghostc in sorted(checked):
                        if (ghostr+rd,ghostc+cd) not in checked:
                            data[ghostr+rd][ghostc+cd] = data[ghostr][ghostc]
                            data[ghostr][ghostc] = '.'
                            checked.remove((ghostr,ghostc))
                r,c = rn,cn
        if data[rn][cn] == '#':
            continue

    gps = 0
    for r in range(len(data)):
        for c in range(len(data[r])):
            if data[r][c] in '[O':
                gps += (100*r) + c
    return gps

print(arranger(data,dir,False))
print(arranger(data,dir,True))

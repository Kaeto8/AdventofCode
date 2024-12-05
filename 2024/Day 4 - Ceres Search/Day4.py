with open('data4.txt') as file:
    data = file.readlines()

total, total2, linenumber = 0, 0, 0
for line in data:
    for i in range(len(line)):
        if line[i] == 'X':
            if i-3 >= 0 and line[i-1] == 'M' and line[i-2] == 'A' and line[i-3] == 'S':
                total += 1
            if i+3 < len(line) and line[i+1] == 'M' and line[i+2] == 'A' and line[i+3] == 'S':
                total += 1
            if linenumber-3 >= 0:
                if data[linenumber-1][i] == 'M' and data[linenumber-2][i] == 'A' and data[linenumber-3][i] == 'S':
                    total += 1
                if data[linenumber-1][i+1] == 'M' and data[linenumber-2][i+2] == 'A' and data[linenumber-3][i+3] == 'S':
                    total += 1
                if data[linenumber-1][i-1] == 'M' and data[linenumber-2][i-2] == 'A' and data[linenumber-3][i-3] == 'S':
                    total += 1
            if linenumber+3 < len(data):
                if data[linenumber+1][i] == 'M' and data[linenumber+2][i] == 'A' and data[linenumber+3][i] == 'S':
                    total += 1
                if data[linenumber+1][i+1] == 'M' and data[linenumber+2][i+2] == 'A' and data[linenumber+3][i+3] == 'S':
                    total += 1
                if data[linenumber+1][i-1] == 'M' and data[linenumber+2][i-2] == 'A' and data[linenumber+3][i-3] == 'S':
                    total += 1
        if linenumber != 0 and linenumber != len(data)-1 and i !=0 and i != len(line)-1:
            if line[i] == 'A':
                if data[linenumber-1][i-1] == 'M' and data[linenumber-1][i+1] == 'M' and data[linenumber+1][i-1] == 'S' \
                and data[linenumber+1][i+1] == 'S':
                    total2 += 1
                if data[linenumber-1][i-1] == 'M' and data[linenumber-1][i+1] == 'S' and data[linenumber+1][i-1] == 'M' \
                and data[linenumber+1][i+1] == 'S':
                    total2 += 1
                if data[linenumber-1][i-1] == 'S' and data[linenumber-1][i+1] == 'S' and data[linenumber+1][i-1] == 'M' \
                and data[linenumber+1][i+1] == 'M':
                    total2 += 1
                if data[linenumber-1][i-1] == 'S' and data[linenumber-1][i+1] == 'M' and data[linenumber+1][i-1] == 'S' \
                and data[linenumber+1][i+1] == 'M':
                    total2 += 1
    linenumber+=1

print(total)
print(total2)

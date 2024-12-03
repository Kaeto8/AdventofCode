with open('data2.txt') as file:
    data = file.readlines()

def Analyzer(line):
    good = 0
    safe = False
    for i in range(len(line)-1):
        if (int(line[0])>int(line[1])) and (int(line[i])>int(line[i+1])) and (int(line[i])-int(line[i+1])<=3)== True:
            safe = True
        elif (int(line[0])<int(line[1])) and (int(line[i])<int(line[i+1])) and (int(line[i+1])-int(line[i])<=3)== True:
            safe = True
        else:
            safe = False
            break
    
    if safe==True:
        good = 1
    return good

def SecondAnalyzer(line):
    secondgood = 0
    if not Analyzer(line) == 1:
        for i in range(len(line)):
            newline = line.copy()
            newline.pop(i)
            if Analyzer(newline) == 1:
                secondgood = 1
                break
    return secondgood
    
report = 0
report2 = 0
for line in data:
    line = line.strip().split()
    report += Analyzer(line)
    report2 += SecondAnalyzer(line)
print(report)
print(report+report2)            

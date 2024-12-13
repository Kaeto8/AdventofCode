with open("data9.txt") as file:
    data = file.read()

x = int((len(data)+1)/2)
a , y = 0, []
y1, y2 = [], []

for i in range(x):
    for j in range(int(data[a])):
        y.append(i)
    if a+1 < len(data):
        for k in range(int(data[a+1])):
            y.append('.')
    a+=2

y1 = y.copy()

for i in range(len(y1)):
    if '.' in y1:
        if y1[i] == '.':
            y1[i] = y1[len(y1)-1]
            y1.pop(len(y1)-1)
            while y1[len(y1)-1] == '.':
                y1.pop(len(y1)-1)

y2 = y.copy()
z = y2[len(y2)-1]

for last in range(z, 0, -1):
    a = y2.count(last)
    for i in range(y2.index(last)):
        flag = False
        if y2[i] == '.':
            flag = False
            for j in range(a):
                if y2[i+j] == last:
                    flag = False
                    break
                elif y2[i+j] == '.':
                    flag = True
                else:
                    flag = False
                    break
            if flag:
                while last in y2:
                    index = y2.index(last)
                    y2[index] = '.'
                for k in range(a):
                    y2[i+k] = last
                while y2[len(y2)-1] == '.':
                    y2.pop()
                break

sum1, sum2 = 0,0
for i in range(len(y1)):
    sum1 += i*y1[i]

for i in range(len(y2)):
    if y2[i] != '.':
        sum2 += i*y2[i]

print(sum1, sum2)

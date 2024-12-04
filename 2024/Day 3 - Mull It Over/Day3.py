import re

with open('data3.txt') as file:
    data = file.read()

sum = 0
x = re.findall("mul[(]\d+,\d+[)]", data)

for i in x:
    y = re.findall(r"\d+", i)
    sum += int(y[0])*int(y[1])

print(sum)

#................Part 2..................

sum2 = 0
flag = True
x2 = re.findall(r"mul[(]\d+,\d+[)]|do[(][)]|don't[(][)]", data)

for k in x2:
    if k == "do()":
        flag = True
    elif k == "don't()":
        flag = False
    else:
        if flag:
            c = re.findall(r"\d+", k)
            sum2 += int(c[0])*int(c[1])

print(sum2)

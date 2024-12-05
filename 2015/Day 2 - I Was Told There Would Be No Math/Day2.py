import re

with open('input.txt') as file:
    data = file.readlines()

paper, ribbon = 0, 0
for line in data:
    x = re.findall(r"\d+",line)
    a = int(x[0])*int(x[1])
    b = int(x[1])*int(x[2])
    c = int(x[0])*int(x[2])
    smallest = min(a,b,c)
    paper += 2*(a+b+c) + smallest
    if smallest==a:
        ribbon += (2*(int(x[0])+int(x[1]))) + (int(x[0])*int(x[1])*int(x[2]))
    elif smallest==b:
        ribbon += (2*(int(x[1])+int(x[2]))) + (int(x[0])*int(x[1])*int(x[2]))
    elif smallest==c:
        ribbon += (2*(int(x[0])+int(x[2]))) + (int(x[0])*int(x[1])*int(x[2]))

print(paper)
print(ribbon)

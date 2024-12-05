import re

with open('input.txt') as file:
    data = file.read()

x=[0,0]
y=['0,0']

for char in data:
    if char == '^':
        x[0]+=1
    elif char == '>':
        x[1]+=1
    elif char == '<':
        x[1]-=1
    elif char == 'v':
        x[0]-=1
    y.append(str(x[0])+','+str(x[1]))

print(len(set(y)))

#................Part 2..............

santa=[0,0]
rsanta=[0,0]
y2=['0,0']
i=0

for char in data:
    i+=1
    if i%2==0:
        if char == '^':
            santa[0]+=1
        elif char == '>':
            santa[1]+=1
        elif char == '<':
            santa[1]-=1
        elif char == 'v':
            santa[0]-=1
        y2.append(str(santa[0])+','+str(santa[1]))
    else:
        if char == '^':
            rsanta[0]+=1
        elif char == '>':
            rsanta[1]+=1
        elif char == '<':
            rsanta[1]-=1
        elif char == 'v':
            rsanta[0]-=1
        y2.append(str(rsanta[0])+','+str(rsanta[1]))

print(len(set(y2)))

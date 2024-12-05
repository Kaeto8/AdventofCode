with open('data1.txt') as file:
    data = file.read()

total = 0
found = False
for i in range(len(data)):
    if data[i] == '(':
        total += 1
    elif data[i] == ')':
        total -= 1
    if total == -1 and found == False:
        x = i+1
        found = True

print(total)
print(x)

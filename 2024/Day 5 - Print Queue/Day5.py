with open('data5.txt') as file:
    data = file.readlines()

rules, updates=[], []
total, total2=0,0

for line in data:
    if "|" in line:
        rules.append([int(n) for n in line.split('|')])
    elif "," in line:
        updates.append([int(n) for n in line.split(',')])

book = dict()
for rule in rules:
    if rule[1] not in book.keys():
        book[rule[1]] = {rule[0]}
    else:
        book[rule[1]].update({rule[0]})

def validator(update):
    for i, n in enumerate(update):
        if not book[n].isdisjoint(update[i:]):
            return False
    return True    

for update in updates:
    if validator(update):
        total += update[len(update)//2]
    if not validator(update):
        reorder = []
        copy = set(update)
        while copy:
            for c in copy:
                if book[c].isdisjoint(copy):
                    reorder.append(c)
                    copy.remove(c)
                    break
        total2 += reorder[len(reorder)//2]
print(total)
print(total2)

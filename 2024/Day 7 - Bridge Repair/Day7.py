with open("data7.txt") as file:
    data = file.readlines()

def checker(total, num, cond):
    if len(num)==1:
        return num[0]==total
    elif checker(total, [num[0]+num[1]] + num[2:], cond):
        return True
    elif checker(total, [num[0]*num[1]] + num[2:], cond):
        return True
    elif cond and checker(total, [int(str(num[0])+str(num[1]))] + num[2:], cond):
        return True
    return False

sum, sum2=0,0
for line in data:
    total, num = line.strip().split(':')
    total = int(total)
    num=num.strip().split()
    num = [int(x) for x in num]
    if checker(total, num, cond=False):
        sum += total
    if checker(total, num, cond=True):
        sum2+=total
print(sum)
print(sum2)

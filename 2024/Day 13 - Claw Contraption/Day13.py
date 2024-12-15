import re

with open("data13.txt") as file:
    data = file.read().strip().split('\n\n')

total, total2 = 0, 0
for line in data:
    num = re.findall('\d+', line)
    ax, ay, bx, by, x, y = map(int, num)

    A = (x*by-y*bx)/(ax*by-ay*bx)
    B = (ax*y-ay*x)/(ax*by-ay*bx)
    x += 10000000000000
    y += 10000000000000
    A2 = (x*by-y*bx)/(ax*by-ay*bx)
    B2 = (ax*y-ay*x)/(ax*by-ay*bx)
    A=str(A).removesuffix(".0")
    B=str(B).removesuffix(".0")
    A2=str(A2).removesuffix(".0")
    B2=str(B2).removesuffix(".0")

    if '.' not in A and '.' not in B:
        A, B = int(A), int(B)
        if A <= 100 and B <=100:
            total += 3*A + B
    if '.' not in A2 and '.' not in B2:
        A2, B2 = int(A2), int(B2)
        total2 += 3*A2 + B2

print(total)
print(total2)

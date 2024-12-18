import re
data = open("data17.txt").read().split('\n')

arr=[]
for line in data:
    num = re.findall('\d+', line)
    arr.append(num)

A, B, C = int(arr[0][0]), int(arr[1][0]), int(arr[2][0])
program = [int(x) for x in arr[4]]

def debugger(program, A):
    def combo(x):
        if x in [0,1,2,3]:
            return x
        if x == 4:
            return A
        if x == 5:
            return B
        if x == 6:
            return C
    B = 0
    C = 0
    ip, output = 0,[]
    while ip < len(program):
        if program[ip] == 0:
            A = A//pow(2, combo(program[ip+1]))
        elif program[ip] == 1:
            B = B^program[ip+1]
        elif program[ip] == 2:
            B = combo(program[ip+1])%8
        elif program[ip] == 3:
            if A != 0:
                ip = program[ip+1]
                ip -= 2
        elif program[ip] == 4:
            B = B^C
        elif program[ip] == 5:
            output.append(combo(program[ip+1])%8)
        elif program[ip] == 6:
            B = A//pow(2, combo(program[ip+1]))
        elif program[ip] == 7:
            C = A//pow(2, combo(program[ip+1]))
        ip += 2
    return output

output = debugger(program, A)
print(','.join([str(x) for x in output]))

def a_reg(A=0, index=len(program)-1):
    if index < 0:
        return A
    for i in range(8):
        output = debugger(program, A*8+i)
        if output[0] == program[index]:
            if result := a_reg((A*8+i), index-1): 
                return result
    return
print(a_reg())

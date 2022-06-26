t = int(input())
memory = []
testcase = []
for i in range(t):
    testcase.append(int(input()))
memory.append(1)
memory.append(2)
memory.append(4)
for i in range(8):
    sum = 0
    for j in range(3):
        sum = sum + memory[i+2-j]
    memory.append(sum)
for i in testcase:
    print(memory[i-1])
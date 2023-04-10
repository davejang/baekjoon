def solution(arr):
    stack = []
    temp = ""
    for i in arr:
        if i == temp:
            continue
        stack.append(i)
        temp = i
    return stack
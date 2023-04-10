def solution(s):
    stack = []
    for c in s:
        if c == '(' or c == '[':
                stack.append(c)
        if not stack:
            if c == ')' or c == ']':
                return False
        if stack:
            if c == ')':
                if stack.pop() == '(':
                    continue
                else:
                    return False
            if c == ']':
                if stack.pop() == '[':
                    continue
                else:
                    return False
    if stack:
        return False
    if not stack:
        return True
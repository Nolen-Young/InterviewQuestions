def isValid(s: str) -> bool:
    parenMap = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = []
    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        else:
            test = stack.pop()
            if parenMap[test] != char:
                return False
            
    if len(stack) > 0:
        return False
    else:
        return True

print(isValid('()'))
if __name__ == "__main__":
    infix = input()
    stack = []
    pr = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}  # 연산자 집합
    operand = ''
    postfix = []
    for tmp in infix:
        if tmp in "+-*/":
            if operand != '':
                postfix.append(int(operand))
                operand = ''
            while stack and pr[tmp] <= pr[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(tmp)
        elif tmp == "(":
            stack.append(tmp)
        elif tmp == ")":
            postfix.append(int(operand))
            operand = ''
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            operand += tmp
    postfix.append(int(operand))
    while stack:
        postfix.append(stack.pop())

    print(postfix)

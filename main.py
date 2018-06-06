def validate(to_validate):  # 올바른 입력이면 True를 반환, 반대는 False
    if to_validate == '':  # 아무것도 입력하지 않았다면
        print('수식을 입력해주세요')
        return False
    was_oper = True  # 이전에 봤던 문자가 연산자였는지 저장합니다
    opened_parenthesis = 0  # 열려있는 괄호의 개수를 저장합니다
    was_opened = False
    for tmp in to_validate:
        if tmp in "+-*/":
            if was_oper:
                print('Infix 형식이 맞는지 확인해주세요')  # 중위표현에서 연산자가 연달아 있으면 문제가 됩니다.
                return False
            was_oper = True
            was_opened = False
        elif tmp in "1234567890":
            was_oper = False  # 숫자는 연달아 있던 아니던 상관이 없습니다
            was_opened = False
        elif tmp == '(':
            opened_parenthesis += 1
            was_opened = True
        elif tmp == ')':
            if was_opened:
                print('괄호의 표현에 문제가 있습니다')
                return False
            if opened_parenthesis < 1:
                print('괄호짝이 맞지 않습니다')
                return False
            opened_parenthesis -= 1
            was_opened = False
    if opened_parenthesis != 0:
        print('괄호짝이 맞지 않습니다')
        return False
    return True


def print_postfix(postfix):
    postfix_str = ''
    for tmp in postfix:
        postfix_str += str(tmp) + ' '
    print('Postfix:', postfix_str)


def calc(result):
    stack = []
    for i in result:
        if str(i) == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(b + a)
        elif str(i) == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif str(i) == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        elif str(i) == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        else:
            stack.append(i)

    print('Result:', stack.pop())


if __name__ == "__main__":
    operator = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}  # 연산자 집합
    operand = ''
    stack = []
    postfix = []
    while True:
        infix = input('Infix: ')
        if validate(infix):
            break

    for tmp in infix:
        if tmp in "+-*/":
            if operand != '':
                postfix.append(int(operand))
                operand = ''
            while stack and operator[tmp] <= operator[stack[-1]]:
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

    print_postfix(postfix)  # 변환된 식 출력
    calc(postfix)  # 계산 후 결과 출력

def validate(to_validate):  # 올바른 입력이면 True를 반환, 반대는 False
    if to_validate == '':  # 아무것도 입력하지 않았다면
        print('수식을 입력해주세요')
        return False

    # 피연산자와 연산자의 개수를 비교하고 의도치 않은 문자가 있는지 확인하는 파트
    was_operand = False  # 이전에 봤던 문자가 피연산자의 일부였는지 저장합니다
    operand_num = 0
    operator_num = 0
    for i in to_validate:
        if i in "+-*/":
            operator_num += 1
            was_operand = False
        elif i in "1234567890":
            if not was_operand:
                operand_num += 1
                was_operand = True
    if operator_num >= operand_num:
        print('연산자의 개수가 피연산자의 개수와 같거나 더 많습니다')
        return False

    # infix 형식 확인과 괄호 표현 확인하는 파트
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
            if was_opened:  # 괄호를 열자마자 닫는 경우입니다
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

    # 예외가 없다면 입력무한루프 탈출
    return True


def check_num(postfix):  # 연산자와 피연산자의 개수를 비교합니다
    operator_num = 0
    operand_num = 0
    for i in postfix:
        if i in "+-*/":
            operator_num += 1
        elif i in "1234567890":
            operand_num += 1
    if operator_num >= operand_num:
        print('연산자의 개수가 피연산자의 개수보다 많습니다')
        return False
    return True


def print_postfix(postfix):  # Postfix로 변환된 수식을 출력합니다
    postfix_str = ''
    for tmp in postfix:
        postfix_str += str(tmp) + ' '
    print('Postfix:', postfix_str)


def calc(result):  # 후위표기식의 연산은 간단합니다.
    stack = []
    for i in result:
        # 연산자가 나오면 스택에 쌓인 두개의 값을 pop 하여 연산 후 다시 스택에 push를 반복합니다.
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
        else:  # 숫자가 나오면 계속 스택에 push 합니다
            stack.append(i)

    print('Result:', stack.pop())


if __name__ == "__main__":
    operator = {"(": 0, ")": 0, "+": 1, "-": 1, "*": 2, "/": 2}  # 연산자 집합
    operand = ''
    stack = []
    postfix = []
    # 예외처리를 위한 무한루프
    while True:
        infix = input('Infix: ')
        if validate(infix):
            break

    # Postfix 변환 파트
    for tmp in infix:
        if tmp in "+-*/":  # 연산자를 만나면
            if operand != '':
                postfix.append(int(operand))  # 앞에서 꺼내던 피연산자를 Postfix에 올립니다
                operand = ''
            while stack and operator[tmp] <= operator[stack[-1]]:  # 스택이 비어있지 않거나 앞의 연산자보다 우선순위가 높은 연산자라면
                postfix.append(stack.pop())  # Postfix로 계속 꺼내옵니다
            stack.append(tmp)
        elif tmp == "(":  # 여는 괄호
            stack.append(tmp)
        elif tmp == ")":
            postfix.append(int(operand))  # 앞에서 꺼내던 피연산자를 Postfix에 올립니다
            operand = ''
            while stack and stack[-1] != "(":  # 스택이 비어있지 않거나 여는 괄호를 만나지 않는 동안
                postfix.append(stack.pop())  # Postfix로 계속 꺼내옵니다
            stack.pop()
        else:
            operand += tmp  # 문자 하나만 읽을 수 있기에 피연산자라면 쌓아놓고 연산자를 만났을 때 Postfix에 올립니다
    postfix.append(int(operand))  # 식은 피연산자로 끝나기에 마지막 피연산자는 따로 Postfix에 올려줍니다
    while stack:
        postfix.append(stack.pop())

    print_postfix(postfix)  # 변환된 식 출력
    calc(postfix)  # 계산 후 결과 출력

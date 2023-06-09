# 根据运算符运算
def operate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2


def evaluate(expression):
    # 数字栈和运算符栈
    stack_num = []
    stack_op = []
    # 运算优先级
    operators_proiority = {'+':1, '-':1, '*':2, '/':2}

    for i in range(len(expression)):
        # 读取数字, 可能是多位数
        if expression[i].isdigit():
            current_number = 0
            while i<len(expression) and expression[i].isdigit():
                current_number = current_number * 10 + int(expression[i])
                i+=1
            # 这是一个数字
            stack_num.append(current_number)
        # 运算符
        else:
            # 这个运算符优先级大于栈顶运算符优先级, 直接入栈,不计算
            # 比如3 + 5 * 8 / 4,
            # 遇到了+,直接入栈,
            # 遇到了*,直接入栈,
            # 遇到/时,栈顶是*,优先级等于/,计算5*8,再入栈
            # 变成3 + 40 / 4,栈顶是+,优先级小于/,不运算
            # 数字栈是3 40 4
            # 符号栈是+ /
            # 出了for 进入while
            # 先计算40/4,再入栈
            # 在计算3+10
            # 结果13
            if stack_op and operators_proiority[expression[i]] > operators_proiority[stack_op[-1]]:
                stack_op.append(expression[i])
            else:
                # 如果栈顶的运算符优先级大于等于当前运算符,那么就计算
                while stack_op and operators_proiority[expression[i]] <= operators_proiority[stack_op[-1]]:
                    num2 = stack_num.pop()
                    num1 = stack_num.pop()
                    op = stack_op.pop()
                    stack_num.append(operate(num1, num2, op))
                stack_op.append(expression[i])
    # 处理栈中剩余元素
    while stack_op:
        num2 = stack_num.pop()
        num1 = stack_num.pop()
        op = stack_op.pop()
        stack_num.append(operate(num1, num2, op))
    return stack_num.pop()
evaluate('3+5*8/4')
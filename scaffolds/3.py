# a op b op c op d
# op表示运算符计算的次序
# 共有6中次序
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# 对应的表达式
# a*b*c*d
# (a*b)*(c*d)
# a*(b*c)*d
# a*((b*c)*d)
# (a*b)*(c*d)
# a*(b*(c*d))

import itertools
import random

def calculate_24(nums):
    # 从运算符中选取3个运算符,共有64种可能
    for ops in itertools.product(['+', '-', '*', '/'], repeat=3):
        a, b, c, d = nums
        
        # 根据之前的次序,添加括号计算
        # Try a+b+c+d
        try:
            if eval(f'{a}{ops[0]}{b}{ops[1]}{c}{ops[2]}{d}') == 24:
                print(f'{a}{ops[0]}{b}{ops[1]}{c}{ops[2]}{d}')
                return True
        except ZeroDivisionError:
            pass
        # Try (a*b)*(c*d)
        try:
            if eval(f'({a}{ops[0]}{b}){ops[1]}({c}{ops[2]}{d})') == 24:
                print(f'({a}{ops[0]}{b}){ops[1]}({c}{ops[2]}{d})')
                return True
        except ZeroDivisionError:
            pass
        # Try a*(b*c)*d
        try:
            if eval(f'{a}{ops[0]}({b}{ops[1]}{c}){ops[2]}{d}') == 24:
                print(f'{a}{ops[0]}({b}{ops[1]}{c}){ops[2]}{d}')
                return True
        except ZeroDivisionError:
            pass
        # Try a*((b*c)*d)
        try:
            if eval(f'{a}{ops[0]}(({b}{ops[1]}{c}){ops[2]}{d})') == 24:
                print(f'{a}{ops[0]}(({b}{ops[1]}{c}){ops[2]}{d})')
                return True
        except ZeroDivisionError:

            pass
        # Try (a*b)*(c*d)
        try:
            if eval(f'({a}{ops[0]}{b}){ops[1]}({c}{ops[2]}{d})') == 24:
                print(f'({a}{ops[0]}{b}){ops[1]}({c}{ops[2]}{d})')
                return True
        except ZeroDivisionError:
            pass
        # Try a*(b*(c*d))
        try:
            if eval(f'{a}{ops[0]}({b}{ops[1]}({c}{ops[2]}{d}))') == 24:
                print(f'{a}{ops[0]}({b}{ops[1]}({c}{ops[2]}{d}))')
                return True
        except ZeroDivisionError:
            pass
    return False
# 随机生成4个数字
nums = [random.randint(1, 10) for _ in range(4)]
if calculate_24(nums):
    print(f'{nums} can be calculated to 24!')
else:
    print(f'{nums} cannot be calculated to 24, trying again...')
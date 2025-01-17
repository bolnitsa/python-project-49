import random


GAME_RULES = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 100


def calculate(left_num, operator, right_num):
    if operator == '+':
        return left_num + right_num
    elif operator == '-':
        return left_num - right_num
    elif operator == '*':
        return left_num * right_num
    else:
        raise ValueError("Unknown operator: {}".format(operator))


def play():
    operators = ['+', '-', '*']

    operator = random.choice(operators)
    left_num = random.randint(MIN_NUM, MAX_NUM)
    right_num = random.randint(MIN_NUM, MAX_NUM)

    expression = f'{left_num} {operator} {right_num}'
    correct_answer = str(calculate(left_num, operator, right_num))

    return expression, correct_answer

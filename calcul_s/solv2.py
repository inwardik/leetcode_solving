import unittest
import random

def get_list(input_string):
    result = []
    temp = ''
    for item in input_string:
        if item.isnumeric():
            temp += item
        else:
            if temp:
                result.append(int(temp))
            result.append(item)
            temp = ''
    if temp:
        result.append(int(temp))
    return result
def eq(num1, num2, sign):
    if sign == '+':
        return num2 + num1
    elif sign == '-':
        return num2 - num1
    elif sign == '*':
        return num2 * num1
    elif sign == '/':
        return num2 / num1
priority = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    ')': 0,
    '(': 0,
}
def my_calc(input_string):
    data = get_list(input_string)
    numbers, signs = [], []
    for item in data:
        if isinstance(item, int):
            numbers.append(item)
        else:
            if item == ')' and signs[-1] == '(':
                signs.pop()
                continue
            while signs and len(numbers) > 1 and priority[signs[-1]] >= priority[item] and signs[-1] != '(' and item != '(':
                numbers.append(eq(numbers.pop(), numbers.pop(), signs.pop()))
            if item == ')' and signs[-1] == '(':
                signs.pop()
            else:
                signs.append(item)
    while signs and len(numbers) > 1:
        numbers.append(eq(numbers.pop(), numbers.pop(), signs.pop()))
    return numbers


def r():
    return str(random.randint(1, 50)) + random.choice(['+', '-', '*', '/'])

i = ''.join([r() for i in range(10)])[:-1]
t1 = '46+(46*(28+21)/6*16+4)-14-1/1'
t2 = '39/(29*21)/17/34*25/(6+38*1)+9'
t3 = '9-(19-11)+(46-17)*28*(45-43-39-12)'
t4 = '40/(11+44/30)/28*(39+50)+8/45-3'
tlist = [t1, t2, t3, t4]
for t in tlist:
    print(t)
    print(eval(t))
    print(my_calc((t)))

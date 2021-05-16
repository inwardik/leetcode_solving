def gen_num(expr):
    temp = ''
    for num in expr:
        if num.isdigit():
            temp += num
        else:
            yield int(temp)
            temp = ''
            yield num
    yield int(temp)

def ev(num1, num2, sign):
    if sign == '+':
        return num2 + num1
    elif sign == '-':
        return num2 - num1
    elif sign == '*':
        return num2 * num1
    elif sign == '%':
        return num2 / num1
    else:
        raise ValueError('wrong sign')



def calcul(expr):
    sign_prior = {'-': 1, '+': 1, '*': 2, '%': 2}
    g = list(gen_num(expr))
    digits = []
    signs = []
    for i, ch in enumerate(g):
        if isinstance(ch, int):
            if digits and signs:
                if i < len(g)-1 and sign_prior[g[i+1]] > sign_prior[signs[-1]]:
                    digits.append(ch)
                else:
                    digits.append(ev(ch, digits.pop(), signs.pop()))
            else:
                digits.append(ch)
        else:
            signs.append(ch)
    while signs and len(digits) > 1:
        digits.append(ev(digits.pop(), digits.pop(), signs.pop()))

    return digits



expr = '22+4*2-12+2'
res = calcul(expr)
print(res)
from collections import deque


def p(op,lvl):

    if op == '+' or op == '-':
        return 1 + lvl
    elif op == '*' or op == '/':
        return 2 + lvl
    else:
        return 0 + lvl


def Calc(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


if __name__ == "__main__":

    exp = "10+30+(50-(((89*15-3)/20*500-23+16*97-36)*200/10-3+1)*40/10)+5-4*2"
    if not exp:
        exp = input()

    stackNumbers = deque() # stiva variabile / operanzi
    stackOperators = deque() # stiva operatori

    lvl_precedenta = 0
    nr = None

    exp += '\n'
    for c in exp:

        if c.isdigit():
            if nr == None:
                nr = 0
            nr = nr * 10 + ord(c) - ord('0')

        else:
            if nr != None:
                #print(nr)
                stackNumbers.append(nr)

            if c == '(':
                lvl_precedenta += 10

            elif c == ')':
                lvl_precedenta -= 10

            else:

                while stackOperators and p(c, lvl_precedenta) <= p(stackOperators[-1][0], stackOperators[-1][1]):

                    result = Calc(stackNumbers[-2], stackNumbers[-1], stackOperators[-1][0])
                    stackNumbers.pop()
                    stackNumbers.pop()
                    stackOperators.pop()
                    stackNumbers.append(result)

                stackOperators.append([c,lvl_precedenta])

            nr = None

    print(stackNumbers[0])

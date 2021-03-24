from collections import deque


def p(op,lvl):

    if op == '+' or op == '-':
        return 1 + lvl
    elif op == '*' or op == '/':
        return 2 + lvl
    else:
        return 0 + lvl


if __name__ == "__main__":

    #exp = "a+b+(a-b/c)+d-e*c"
    exp = "c*(a+b)"
    if not exp:
        exp = input()

    stackAlpha= deque() # stiva variabile / operanzi
    stackOperators = deque() # stiva operatori

    lvl_precedenta = 0
    nr = None

    exp += '\n'
    for c in exp:

        if c.isalpha():
            print("Adaug pe stiva de variabile operandul '{}'".format(c))
            stackAlpha.append(c)

        else:
            if c == '(':
                lvl_precedenta += 10

            elif c == ')':
                lvl_precedenta -= 10

            else:
                while stackOperators and p(c, lvl_precedenta) <= p(stackOperators[-1][0], stackOperators[-1][1]):

                    print("Combin operanzii '{}' si '{}' cu operatorul '{}'".format(stackAlpha[-2],stackAlpha[-1], stackOperators[-1][0]))
                    result = stackAlpha[-2] + stackOperators[-1][0] + stackAlpha[-1]

                    stackAlpha.pop()
                    stackAlpha.pop()
                    stackOperators.pop()

                    print("Adaug pe stiva de variabile '{}'".format(result))
                    stackAlpha.append(result)

                if c != ' ' and c != '\n':
                    print("Adaug pe stiva de operatori '{}' cu precendeta {}".format(c,p(c,0)+lvl_precedenta))
                    stackOperators.append([c,lvl_precedenta])

    print("\nSirul rezultat este '{}'".format(stackAlpha[0]))

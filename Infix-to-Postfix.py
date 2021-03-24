from collections import deque


def precedence(op):
    if op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    else:
        return 0


def print_step(res, stack):
    print(res, end='       ')
    print(''.join(stack))


def reconstructie(exp):
    stack = deque()

    for chr in exp:
        if chr.isalpha():
            stack.append(chr)
        else:
            op1 = stack[-1]
            stack.pop()
            op2 = stack[-1]
            stack.pop()
            stack.append(op2 + chr + op1)
            print("Combinam {}, {}, {}".format(op2,chr,op1))
            print(stack[-1])

    return stack[-1]


if __name__ == "__main__":
    #exp = "a+b*(c*d-e)*(f+g*h)-i"
    #exp = "(a+b*(a-c/d)+(a-l))/r+h"
    exp = "a*(b-c)+d"
    res = ""

    stack = deque()

    print("SIR POLONEZ   STIVA\n")

    for chr in exp:
        if chr == ' ':
            continue

        if chr.isalpha():
            res += chr
            print_step(res, stack)

        elif chr == '(':
            stack.append(chr)
            print_step(res, stack)

        elif chr == ')':
            # scot totul din stiva pana la '('
            while stack[-1] != '(':
                res += stack[-1]
                stack.pop()
                print_step(res, stack)

            stack.pop()
            print_step(res, stack)

        else:
            # scoatem din stiva cat timp precedenta e mai mica
            while stack and precedence(chr) <= precedence(stack[-1]):
                res += stack[-1]
                stack.pop()
                print_step(res, stack)

            # adaugam in stiva
            stack.append(chr)
            print_step(res, stack)

    # scoatem ce a ramas din stiva
    while stack:
        res += stack[-1]
        stack.pop()
        print_step(res, stack)

    print("\nSirul polonez: {}\n\n\n".format(res))

    print('\nSirul reconstruit: ' + reconstructie(res))




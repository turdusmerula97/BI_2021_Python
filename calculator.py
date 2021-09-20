a = float(input())
c = str(input())
b = float(input())

if (c == '/' or c == 'mod' or c == 'div') and b == 0:
    print('Деление на 0')
elif c == '/':
    print(a / b)
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == "*":
    print(a * b)
elif c == '%':
    print(a % b)
elif c == '//':
    print(a // b)
elif c == '^':
    print(a ** b)
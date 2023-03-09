expression = []

while '' not in expression:
    number = int(input("Введите чиcло : "))
    expression.append(number)
    action = input("Введите арифметическое действие ( - , +, *, / ) или нажмите Enter для вычисления выражения: ")
    expression.append(action)

for division_or_multiplication in expression:
    for div in expression:
        if div == '*':
            index = expression.index('*')
            previous_index = index - 1
            expression.pop(index)
            y = expression.pop(index)
            x = expression.pop(previous_index)
            new_number = x * y
            expression.insert(previous_index, new_number)
        if div == '/':
            index = expression.index('/')
            previous_index = index - 1
            expression.pop(index)
            y = expression.pop(index)
            x = expression.pop(previous_index)
            new_number = x / y
            expression.insert(previous_index, new_number)

for summ_or_subtraction in expression:
    for ss in expression:
        if ss == '+':
            index = expression.index('+')
            previous_index = index - 1
            expression.pop(index)
            y = expression.pop(index)
            x = expression.pop(previous_index)
            new_number = x + y
            expression.insert(previous_index, new_number)
        if ss == '-':
            index = expression.index('-')
            previous_index = index - 1
            expression.pop(index)
            y = expression.pop(index)
            x = expression.pop(previous_index)
            new_number = x - y
            expression.insert(previous_index, new_number)

print("Result : " + str(expression.pop(0)))

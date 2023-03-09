expression = []


def input_expression():
    while '' not in expression:
        try:
            number = float(input("Enter the number : "))
        except:
            number = float(input("Error, invalid format, please enter a number : "))
        expression.append(number)
        action = input("Enter arithmetic operation ( - , +, *, / ) or press enter to evaluate the expression: ")
        expression.append(action)


def division_or_multiplication():
    for div_or_mult in expression:
        for div_or_mult in expression:
            if div_or_mult == '*':
                index = expression.index('*')
                previous_index = index - 1
                expression.pop(index)
                y = expression.pop(index)
                x = expression.pop(previous_index)
                new_number = x * y
                expression.insert(previous_index, new_number)
            if div_or_mult == '/':
                index = expression.index('/')
                previous_index = index - 1
                expression.pop(index)
                y = expression.pop(index)
                x = expression.pop(previous_index)
                new_number = x / y
                expression.insert(previous_index, new_number)


def summ_or_subtraction():
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


input_expression()
division_or_multiplication()
summ_or_subtraction()

print("Result : " + str(expression.pop(0)))

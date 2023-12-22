def calculate_recursive(expression):
    if isinstance(expression, list):
        operand1 = calculate_recursive(expression[1])
        operand2 = calculate_recursive(expression[2])
        operator = expression[0]
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2
    else:
        return expression

# пример
expr = ['+', 5, ['*', 3, 2]]  # результат: 11
result = calculate_recursive(expr)
print(result)

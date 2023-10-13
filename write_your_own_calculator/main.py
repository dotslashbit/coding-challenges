def get_input():
    # take the expression as input from the user
    s = input()
    return s


def apply_operation(operators, values):
    # Pop an operator and two values from the stacks, perform the operation, and push the result back
    op = operators.pop()
    right = values.pop()
    left = values.pop()

    if op == '+':
        values.append(left + right)
    elif op == '-':
        values.append(left - right)
    elif op == '*':
        values.append(left * right)
    elif op == '/':
        values.append(left / right)

def precedence(op):
    # Define precedence levels for operators
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    return 0

def evaluate(expression):
    values = []       # Stack to hold operands
    operators = []    # Stack to hold operators

    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        if expression[i].isdigit():
            # If a digit is found, extract the entire number and push it onto the operand stack
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.append(int(expression[i:j]))
            i = j
        elif expression[i] == '(':
            operators.append(expression[i])  # Push opening bracket onto the operator stack
            i += 1
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operation(operators, values)  # Apply operations until opening bracket is found
            operators.pop()  # Pop the opening bracket
            i += 1
        else:
            while (operators and precedence(operators[-1]) >= precedence(expression[i])):
                apply_operation(operators, values)  # Apply higher precedence operations
            operators.append(expression[i])  # Push lower precedence operator onto the stack
            i += 1

    while operators:
        apply_operation(operators, values)  # Apply remaining operations

    return values[0]  # The final result is the only value remaining in the operand stack




def calculate(expression):
    try:
        return evaluate(expression)  # Call evaluate function to get the final result
    except:
        return "Expression not valid"  # Handle any exceptions during evaluation


expression = get_input()
result = calculate(expression)
print(f"The result of the expression '{expression}' is: {result}")

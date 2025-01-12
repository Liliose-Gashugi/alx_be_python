def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: add. substract, multiply, or divide.


    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'substract', 'multiply', 'divide').

    Returns:
    float or str: The result of the operation or an error message for invalid operations.


    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'substract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."
    
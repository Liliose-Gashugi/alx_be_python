def safe_divide(numerator, denominator):
    """

    Perform division while handling errors such as division by zero and non-numeric input

    Parameters:
        numerator: The numerator for the division
        denominator: The denominator for the division

        Returns:
        str: The result of the division or an appropriate error message
    """

    try:
        numerator = float(numerator)
        denominator = float(denominator)

        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

    
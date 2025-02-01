
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Return the sum of two numbers.
        This method does not require access to any class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Print the class attribute 'calculation_type' and return the product of two numbers.
        This method has access to class-level attributes via the 'cls' parameter.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
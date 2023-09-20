class MathFunctions:
    """
    A class that provides basic math functions such as addition, division, multiplication, and modulo.

    Methods:
        - `add(num1, num2)`: Adds two numbers and returns the result.
        - `divide(num1, num2)`: Divides num1 by num2 and returns the result.
        - `multiply(num1, num2)`: Multiplies two numbers and returns the result.
        - `modulo(num1, num2)`: Computes the modulo of num1 by num2 and returns the result.
    """

    def add(self, num1, num2):
        """
        Adds two numbers and returns the result.

        :param num1: The first number.
        :type num1: float or int
        :param num2: The second number.
        :type num2: float or int
        :return: The result of the addition.
        :rtype: float or int
        """
        return num1 + num2

    def divide(self, num1, num2):
        """
        Divides num1 by num2 and returns the result.

        :param num1: The numerator.
        :type num1: float or int
        :param num2: The denominator.
        :type num2: float or int
        :return: The result of the division.
        :rtype: float
        :raises ZeroDivisionError: If num2 is 0.
        """
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return num1 / num2

    def multiply(self, num1, num2):
        """
        Multiplies two numbers and returns the result.

        :param num1: The first number.
        :type num1: float or int
        :param num2: The second number.
        :type num2: float or int
        :return: The result of the multiplication.
        :rtype: float or int
        """
        return num1 * num2

    def modulo(self, num1, num2):
        """
        Computes the modulo of num1 by num2 and returns the result.

        :param num1: The dividend.
        :type num1: int
        :param num2: The divisor.
        :type num2: int
        :return: The result of the modulo operation.
        :rtype: int
        :raises ZeroDivisionError: If num2 is 0.
        """
        if num2 == 0:
            raise ZeroDivisionError("Modulo by zero is not allowed.")
        return num1 % num2

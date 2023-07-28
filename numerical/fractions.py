"""
Implements the Fraction class in charge of numeric fractions
"""


class Fraction:
    """
    Class in charge of numeric fractions
    """
    def __init__(self, numerator: float | int = 0, denominator: float | int = 1):
        """
        Constructor for Fraction class
        :param numerator: float or int
        :param denominator: float or int (cannot be zero)
        """
        if not (isinstance(numerator, float) or isinstance(numerator, int)):
            raise TypeError('Numerator must be float or int')
        if not (isinstance(denominator, float) or isinstance(denominator, int)):
            raise TypeError('Denominator must be float or int')
        if denominator == 0:
            raise ZeroDivisionError("Denominator must not be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __str__(self) -> str:
        """
        Converts the fraction to string
        :return: string representation
        """
        return f'{self.numerator}/{self.denominator}'

    def __float__(self):
        """
        Converts the fraction to float
        :return: float representation
        """
        return self.numerator / self.denominator

    def __int__(self):
        """
        Converts the fraction to integer
        :return: integer representation
        """
        return int(self.__float__())

    def simplify(self):
        """
        Simplifies the fraction
        :return: None
        """
        if (self.numerator >= 0 and self.denominator >= 0) or (self.numerator < 0 and self.denominator < 0):
            self.numerator = abs(self.numerator)
        else:
            self.numerator = -abs(self.numerator)
        self.denominator = abs(self.denominator)
        while int(self.numerator) != self.numerator or int(self.denominator) != self.denominator:
            self.numerator *= 10
            self.denominator *= 10
        for num in range(int(self.denominator), 0, -1):
            if self.numerator % num == 0 and self.denominator % num == 0:
                self.numerator = int(self.numerator / num)
                self.denominator = int(self.denominator / num)
                break

    def reverse(self):
        """
        Returns the reverted fraction
        :return: reverted fraction
        """
        if self.numerator != 0:
            return Fraction(self.denominator, self.numerator)
        else:
            return Fraction(0, 1)

    def __add__(self, other):
        """
        Adds fraction or number to fraction
        :param other: fraction or number
        :return: fraction
        """
        result = Fraction()
        if isinstance(other, Fraction):
            result.numerator = self.numerator * other.denominator + other.numerator*self.denominator
            result.denominator = self.denominator*other.denominator
        elif isinstance(other, int) or isinstance(other, float):
            result.numerator = self.numerator + self.denominator*other
            result.denominator = self.denominator
        else:
            raise TypeError('Fraction can be added only to fraction or number')
        result.simplify()
        return result

    def __sub__(self, other):
        """
        Subtracts fraction or number from fraction
        :param other: fraction or number
        :return: fraction
        """
        result = Fraction()
        if isinstance(other, Fraction):
            result.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            result.denominator = self.denominator * other.denominator
        elif isinstance(other, int) or isinstance(other, float):
            result.numerator = self.numerator - self.denominator * other
            result.denominator = self.denominator
        else:
            raise TypeError('Fraction can be added only to fraction or number')
        result.simplify()
        return result

    def __mul__(self, other):
        """
        Multiplies fraction or number to fraction
        :param other: fraction or number
        :return: fraction
        """
        result = Fraction()
        if isinstance(other, Fraction):
            result.numerator = self.numerator * other.numerator
            result.denominator = self.denominator * other.denominator
        elif isinstance(other, int) or isinstance(other, float):
            result.numerator = self.numerator * other
            result.denominator = self.denominator
        else:
            raise TypeError('Fraction can be added only to fraction or number')
        result.simplify()
        return result

    def __truediv__(self, other):
        """
        Divides fraction or number from fraction
        :param other: fraction or number
        :return: fraction
        """
        result = Fraction()
        if isinstance(other, Fraction):
            result.numerator = self.numerator * other.denominator
            result.denominator = self.denominator * other.numerator
        elif isinstance(other, int) or isinstance(other, float):
            result.numerator = self.numerator
            result.denominator = self.denominator * other
        else:
            raise TypeError('Fraction can be added only to fraction or number')
        result.simplify()
        return result

    def __eq__(self, other):
        """
        Overloads the == operator
        :param other: any
        :return: bool
        """
        if isinstance(other, int) or isinstance(other, float):
            return float(self) == other
        elif isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return False

    def __ne__(self, other):
        """
        Overloads the != operator
        :param other: any
        :return: bool
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Overloads the > operator
        :param other: any
        :return: bool
        """
        return float(self) > float(other)

    def __ge__(self, other):
        """
        Overloads the >= operator
        :param other: any
        :return: bool
        """
        return float(self) >= float(other)

    def __lt__(self, other):
        """
        Overloads the < operator
        :param other: any
        :return: bool
        """
        return float(self) < float(other)

    def __le__(self, other):
        """
        Overloads the <= operator
        :param other: any
        :return: bool
        """
        return float(self) <= float(other)


if __name__ == '__main__':
    a = float(input('first numerator: '))
    b = float(input('first denominator: '))
    c = float(input('second numerator: '))
    d = float(input('second denominator: '))
    first = Fraction(a, b)
    second = Fraction(c, d)
    print(f'{first} + {second} = {first + second} ({float(first + second)})')
    print(f'{first} - {second} = {first - second} ({float(first - second)})')
    print(f'{first} * {second} = {first * second} ({float(first * second)})')
    print(f'{first} / {second} = {first / second} ({float(first / second)})')

class Fraction:
    def __init__(self, numerator: float | int = 0, denominator: float | int = 1):
        if not (isinstance(numerator, float) or isinstance(numerator, int)):
            raise TypeError('Numerator must be float or int')
        if not (isinstance(denominator, float) or isinstance(denominator, int)):
            raise TypeError('Denominator must be float or int')
        if denominator == 0:
            raise ZeroDivisionError("Denominator must not be zero")
        if (numerator >= 0 and denominator >= 0) or (numerator < 0 and denominator < 0):
            self.numerator = abs(numerator)
        else:
            self.numerator = -abs(numerator)
        self.denominator = abs(denominator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return int(self.__float__())

    def simplify(self):
        while int(self.numerator) != self.numerator or int(self.denominator) != self.denominator:
            self.numerator *= 10
            self.denominator *= 10
        for num in range(int(self.denominator), 0, -1):
            if self.numerator % num == 0 and self.denominator % num == 0:
                self.numerator = int(self.numerator / num)
                self.denominator = int(self.denominator / num)
                break

    def reverse(self):
        if self.numerator != 0:
            return Fraction(self.denominator, self.numerator)
        else:
            return Fraction(0, 1)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
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
        pass

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        else:
            return float(self) == float(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return float(self) > float(other)

    def __ge__(self, other):
        return float(self) >= float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __le__(self, other):
        return float(self) <= float(other)

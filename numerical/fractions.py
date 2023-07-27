class Fraction:
    def __init__(self, numerator: float | int = 0, denominator: float | int = 1):
        if not (isinstance(numerator, float) or isinstance(numerator, int)):
            raise TypeError('Numerator must be float or int')
        if not (isinstance(denominator, float) or isinstance(denominator, int)):
            raise TypeError('Denominator must be float or int')
        if denominator == 0:
            raise ZeroDivisionError("Denominator must not be zero")
        self.positive = ((numerator >= 0 and denominator >= 0) or (numerator < 0 and denominator < 0))
        self.numerator = abs(numerator)
        self.denominator = abs(denominator)

    def __str__(self):
        if self.positive:
            temp = ''
        else:
            temp = '-'
        return f'{temp}{self.numerator}/{self.denominator}'

    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return int(self.__float__())

    def simplify(self):
        while int(self.numerator) != self.numerator or int(self.denominator) != self.denominator:
            self.numerator *= 10
            self.denominator *= 10
        for num in range(1, int(self.denominator + 1), -1):
            if self.numerator % num == 0:
                self.numerator = int(self.numerator / num)
                self.denominator = int(self.denominator / num)
                break

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        else:
            return float(self) == float(other)

    def __ne__(self, other):
        return not self.__eq__(other)

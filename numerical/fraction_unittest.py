import unittest
from .fractions import Fraction


class MyTestCase(unittest.TestCase):
    def test_zero_in_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            _ = Fraction(5, 0)

    def test_invalid_type_in_numerator(self):
        with self.assertRaises(TypeError):
            _ = Fraction('1', 1)

    def test_invalid_type_in_denominator(self):
        with self.assertRaises(TypeError):
            _ = Fraction(1, '1')

    def test_str_both_positive(self):
        test = Fraction(2, 7)
        result = str(test)
        expected = '2/7'
        self.assertEqual(result, expected)

    def test_str_one_negative(self):
        test = Fraction(2, -7)
        result = str(test)
        expected = '-2/7'
        self.assertEqual(expected, result)

    def test_str_both_negative(self):
        test = Fraction(-2, -7)
        result = str(test)
        expected = '2/7'
        self.assertEqual(expected, result)

    def test_float(self):
        test = Fraction(2, 7)
        result = float(test)
        expected = 2 / 7
        self.assertEqual(expected, result)

    def test_int(self):
        test = Fraction(2, 7)
        result = int(test)
        expected = int(2 / 7)
        self.assertEqual(expected, result)

    def test_simplify_floats(self):
        test = Fraction(1, 0.5)
        test.simplify()
        expected = Fraction(2, 1)
        self.assertEqual(expected, test)

    def test_simplify_ints(self):
        test = Fraction(17, 34)
        test.simplify()
        expected = Fraction(1, 2)
        self.assertEqual(expected, test)

    def test_add(self):
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        result = a + b
        expected = Fraction(5, 4)
        self.assertEqual(expected, result)

    def test_sub(self):
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        result = a - b
        expected = Fraction(-1, 4)
        self.assertEqual(expected, result)

    def test_mul(self):
        a = Fraction(4, 7)
        b = Fraction(1, 2)
        result = a * b
        expected = Fraction(2, 7)
        self.assertEqual(expected, result)

    def test_truediv(self):
        a = Fraction(4, 7)
        b = Fraction(4, 2)
        result = a / b
        expected = Fraction(2, 7)
        self.assertEqual(expected, result)

    def test_eq(self):
        a = Fraction(1, 2)
        b = Fraction(2, 4)
        result = (a == b)
        expected = True
        self.assertEqual(expected, result)

    def test_ne(self):
        a = Fraction(1, 2)
        b = Fraction(2, 4)
        result = (a != b)
        expected = False
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

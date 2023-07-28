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

    def test_add_fraction(self):
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        result = a + b
        expected = Fraction(5, 4)
        self.assertEqual(expected, result)

    def test_add_number(self):
        a = Fraction(3, 4)
        result = a + 1.5
        expected = Fraction(9, 4)
        self.assertEqual(expected, result)

    def test_sub_fraction(self):
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        result = a - b
        expected = Fraction(-1, 4)
        self.assertEqual(expected, result)

    def test_sub_number(self):
        a = Fraction(3, 4)
        result = a - 1.5
        expected = Fraction(-3, 4)
        self.assertEqual(expected, result)

    def test_mul_fraction(self):
        a = Fraction(4, 7)
        b = Fraction(1, 2)
        result = a * b
        expected = Fraction(2, 7)
        self.assertEqual(expected, result)

    def test_mul_number(self):
        a = Fraction(3, 4)
        result = a * 1.5
        expected = Fraction(9, 8)
        self.assertEqual(expected, result)

    def test_truediv_fraction(self):
        a = Fraction(4, 7)
        b = Fraction(4, 2)
        result = a / b
        expected = Fraction(2, 7)
        self.assertEqual(expected, result)

    def test_truediv_number(self):
        a = Fraction(3, 4)
        result = a / 1.5
        expected = Fraction(1, 2)
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

    def test_gt_less(self):
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        result = (a > b)
        expected = False
        self.assertEqual(expected, result)

    def test_gt_greater(self):
        a = Fraction(3, 4)
        b = Fraction(1, 2)
        result = (a > b)
        expected = True
        self.assertEqual(expected, result)

    def test_gt_equal(self):
        a = Fraction(2, 4)
        b = Fraction(1, 2)
        result = (a > b)
        expected = False
        self.assertEqual(expected, result)

    def test_ge_less(self):
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        result = (a >= b)
        expected = False
        self.assertEqual(expected, result)

    def test_ge_greater(self):
        a = Fraction(3, 4)
        b = Fraction(1, 2)
        result = (a >= b)
        expected = True
        self.assertEqual(expected, result)

    def test_ge_equal(self):
        a = Fraction(2, 4)
        b = Fraction(1, 2)
        result = (a >= b)
        expected = True
        self.assertEqual(expected, result)

    def test_lt_less(self):
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        result = (a < b)
        expected = True
        self.assertEqual(expected, result)

    def test_lt_greater(self):
        a = Fraction(3, 4)
        b = Fraction(1, 2)
        result = (a < b)
        expected = False
        self.assertEqual(expected, result)

    def test_lt_equal(self):
        a = Fraction(2, 4)
        b = Fraction(1, 2)
        result = (a < b)
        expected = False
        self.assertEqual(expected, result)

    def test_le_less(self):
        a = Fraction(1, 2)
        b = Fraction(3, 4)
        result = (a <= b)
        expected = True
        self.assertEqual(expected, result)

    def test_le_greater(self):
        a = Fraction(3, 4)
        b = Fraction(1, 2)
        result = (a <= b)
        expected = False
        self.assertEqual(expected, result)

    def test_le_equal(self):
        a = Fraction(2, 4)
        b = Fraction(1, 2)
        result = (a <= b)
        expected = True
        self.assertEqual(expected, result)

    def test_reverse(self):
        test = Fraction(5, 15)
        result = test.reverse()
        expected = Fraction(15, 5)
        self.assertEqual(expected, result)

    def test_reverse_zero(self):
        test = Fraction(0, 15)
        result = test.reverse()
        expected = Fraction(0, 1)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

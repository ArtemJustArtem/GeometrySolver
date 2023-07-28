import unittest
from .expressions import Constant, Variable


class ConstantTestCase(unittest.TestCase):
    def test_invalid_argument(self):
        with self.assertRaises(TypeError):
            _ = Constant('12')

    def test_has_variable(self):
        test = Constant(12)
        self.assertFalse(test.has_variable())

    def test_evaluate(self):
        test = Constant(12)
        result = test.evaluate()
        expected = 12
        self.assertEqual(expected, result)


class VariableTestCase(unittest.TestCase):
    def test_invalid_argument(self):
        with self.assertRaises(TypeError):
            _ = Variable(12)

    def test_has_variable(self):
        test = Variable('x')
        self.assertTrue(test.has_variable())

    def test_evaluate(self):
        test = Variable('x')
        result = test.evaluate(x=12, y=3)
        expected = 12
        self.assertEqual(expected, result)

    def test_evaluate_invalid_argument(self):
        with self.assertRaises(TypeError):
            test = Variable('z')
            _ = test.evaluate(x=12, y=3)


if __name__ == '__main__':
    unittest.main()

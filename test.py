import unittest

class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        for n in 'string', 1.5:
            with self.subTest(x=n):
                self.assertRaises(TypeError, factorize, n)

    def test_negative(self):
        for n in -1, -10, -100:
            with self.subTest(x=n):
                self.assertRaises(ValueError, factorize, n)

    def test_zero_and_one_cases(self):
        for n, f_n in (0, (0, )), (1, (1, )):
            with self.subTest(x=n):
                self.assertEqual(factorize(n), f_n)

    def test_simple_numbers(self):
        for n, f_n in (3, (3, )), (13, (13, )), (29, (29, )):
            with self.subTest(x=n):
                self.assertEqual(factorize(n), f_n)

    def test_two_simple_multipliers(self):
        for n, f_n in (6, (2, 3)), (26, (2, 13)), (121, (11, 11)):
            with self.subTest(x=n):
                self.assertEqual(factorize(n), f_n)

    def test_many_multipliers(self):
        for n, f_n in (1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)):
            with self.subTest(x=n):
                self.assertEqual(factorize(n), f_n)
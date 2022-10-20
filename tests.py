#  Copyright (c) 2022. Illia Popov.

import unittest
import main


class Test(unittest.TestCase):

    def test_pow_1(self):
        # 3^234 mod 17
        self.assertEqual(main.modular_exponentiation(3, 234, 17), pow(3, 234, 17))

    def test_pow_2(self):
        # 3^-(234) mod 17
        self.assertEqual(main.modular_exponentiation(3, -234, 17), pow(3, -234, 17))

    def test_pow_3(self):
        # -3^234 mod 17
        self.assertEqual(main.modular_exponentiation(-3, 234, 17), pow(-3, 234, 17))

    def test_equation_1(self):
        # "13*x ≡ 2 mod 53"
        self.assertEqual(main.solve_equation(13, 2, 53), [45])

    def test_equation_2(self):
        # 10*x ≡ 12 mod 14
        self.assertEqual(main.solve_equation(10, 12, 14), [4, 11])


    def test_inverse_1(self):
        # a*x ≡ 1 mod m
        self.assertEqual(main.modular_multiplicative_inverse(2, 7), pow(2, -1, 7))



if __name__ == '__main__':
    unittest.main(verbosity=2)

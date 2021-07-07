""" TestMaxInteger testing max integer class """
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_default(self):
        self.assertEqual(max_integer(), None)

    def test_first_max(self):
        lista = [60, 5, 3, 32]
        self.assertEqual(max_integer(lista), 60)

    def test_last_max(self):
        lista = [0, 1, 3, 60]
        self.assertEqual(max_integer(lista), 60)

    def test_mixed_max(self):
        lista = [-1, -8, 0, 8, -5]
        self.assertEqual(max_integer(lista), 8)

    def test_max_string(self):
        lista = ['taoufik', 5, 6, 9]
        with self.assertRaises(TypeError):
            max_integer(lista)

if __name__ == "__main__":
    unittest.main()

import unittest

# TRYING OUT UNIT TESTING
class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6)

    def test_sum_double(self):
        self.assertEqual(sum([1.5,2.5,3]), 7)

    def test_sum_fail(self):
        self.assertEqual(sum([1, 1, 3]), 6)
        # assert sum([1, 1, 1]) == 6, "shold be 6"

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split('2222')

if __name__ == '__main__':
    print('something')    # would not print if using $ python -m unittest module.py
    unittest.main()     # run all tests
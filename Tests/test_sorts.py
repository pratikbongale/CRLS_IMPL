import unittest
import Foundations.CH02.insertion_sort as insertion_sort

class TestSortingAlgorithms(unittest.TestCase):

    def __init__(self, sort_func):
        super().__init__()
        self.sort = sort_func

    def test_with_positive_values(self):
        in_arr = [13, 2, 43, 31]
        out_arr = [2, 13, 31, 43]
        self.assertEqual(self.sort(in_arr), out_arr)

    def test_with_negative_values(self):
        in_arr = [-3, 2, -6, 8]
        out_arr = [-6, -3, 2, 8]
        self.assertEqual(self.sort(in_arr), out_arr)

    def test_with_empty_lists(self):
        in_arr = []
        out_arr = []
        self.assertEqual(self.sort(in_arr), out_arr)

    def test_with_random_values(self):
        in_arr = [-3, 2, -6, 8]
        out_arr = [-6, -3, 2, 8]
        self.assertEqual(self.sort(in_arr), out_arr)

if __name__ == '__main__':

    print('Testing:')

    print('Insertion Sort')
    ins_sort = TestSortingAlgorithms(insertion_sort.insertion_sort_inplace)

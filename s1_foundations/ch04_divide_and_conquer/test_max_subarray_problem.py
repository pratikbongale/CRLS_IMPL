import pytest
from s1_foundations.ch04_divide_and_conquer.max_subarray_problem import *

# build test cases
tc_format = "type, input, expected"
tc_values = []

# mixed values
inp = [1, -4, 3, -4]
out = (2, 2, 3)
tc_values.append(('Mixed values', inp, out))

# mixed values
inp = [21, -9, 1, 5, -13, 11, -16]
out = (0, 0, 21)
tc_values.append(('Mixed values', inp, out))

# mixed values
inp = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
out = (7, 10, 43)
tc_values.append(('Mixed values', inp, out))

# negative values
inp = [-7, -2, -3, -3]
out = (1, 1, -2)
tc_values.append(('Negative values', inp, out))

@pytest.fixture(params=
                [
                    max_subarray_brute,
                    max_subarray_crls,
                    pytest.param(max_subarray_linear_basic, marks=pytest.mark.xfail),
                    max_subarray_linear
                ])
def func(request):
    return request.param


@pytest.mark.parametrize(tc_format, tc_values)
def test_all_methods(func, type, input, expected):
    l, h, s = func(input)
    assert (l, h, s) == expected

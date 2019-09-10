import pytest, random

from s1_foundations.ch02_basic_sorts.bubble_sort import bubble_sort_inplace
from s1_foundations.ch02_basic_sorts.insertion_sort import insertion_sort_inplace, insertion_sort_recursive
from s1_foundations.ch02_basic_sorts.merge_sort import merge_sort_inplace, merge_sort_old
from s1_foundations.ch02_basic_sorts.selection_sort import selection_sort_inplace

'''
test cases:
 - positive values
 - negative values
 - mixed values
 - empty lists
 - random values
 - floating point values
 
Note: `==` checks values, `is` checks references
'''

# build test cases
tc_format = "type, input, expected"
tc_values = []

# positive values
inp = [13, 2, 43, 31]
out = sorted(inp)
tc_values.append(('Positive values', inp, out))

# negative values
inp = [-13, -2, -43, -31]
out = sorted(inp)
tc_values.append(('Negative values', inp, out))

# mixed values
inp = [13, -2, -43, 31]
out = sorted(inp)
tc_values.append(('Mixed values', inp, out))

# empty list
inp = []
out = sorted(inp)
tc_values.append(('Empty list', inp, out))

# random values
inp = random.sample(range(-100, 100), 10)
out = sorted(inp)
tc_values.append(('Random values', inp, out))

# floating point
inp = [round(random.random(), 2) for x in range(10)]
out = sorted(inp)
tc_values.append(('Floating point values', inp, out))


@pytest.mark.parametrize( tc_format, tc_values )
def test_insertion_sort(type, input, expected):

    inp_copy = input.copy()
    insertion_sort_inplace(inp_copy)
    assert inp_copy == expected, 'not inplace'

    inp_copy = input.copy()
    insertion_sort_recursive(inp_copy)
    assert inp_copy == expected, 'not inplace'


@pytest.mark.parametrize( tc_format, tc_values )
def test_selection_sort(type, input, expected):

    inp_copy = input.copy()
    selection_sort_inplace(inp_copy)
    assert inp_copy == expected, 'not inplace'


@pytest.mark.parametrize( tc_format, tc_values )
def test_merge_sort(type, input, expected):

    inp_copy = input.copy()
    output = merge_sort_old(inp_copy)
    assert output == expected, 'sorting failed'

    # assuming inp_copy was not changed as old method above is not inplace
    merge_sort_inplace(inp_copy)
    assert inp_copy == expected, 'not inplace / sorting failed'


@pytest.mark.parametrize( tc_format, tc_values )
def test_bubble_sort(type, input, expected):

    inp_copy = input.copy()
    bubble_sort_inplace(inp_copy)
    assert inp_copy == expected, 'not inplace'
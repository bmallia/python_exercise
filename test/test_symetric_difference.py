import pytest

from source.symetric_difference import sym

def test_symetric_diference():
    result =  sym([1, 2, 3], [5, 2, 1, 4]) 
    assert result == [3, 4, 5]

def test_sym_number_elements():
    result = sym([1, 2, 3], [5, 2, 1, 4])
    assert len(result) == 3

def test_sym_duplicated_numbers():
    result = sym([1, 2, 3,3], [5, 2, 1, 4])
    assert result == [3, 4, 5]

def test_sym_duplicated_number_elements():
    result = sym([1, 2, 3,3], [5, 2, 1, 4])
    assert len(result) == 3

def test_sym_sequence_2_ok():
    result = sym([1, 2, 3], [5, 2, 1, 4, 5])
    assert result == [3,4,5]

def test_sym_sequence_2_number_elements():
    result = sym([1, 2, 3], [5, 2, 1, 4, 5])
    assert len(result) == 3

def test_sym_three_sets():
    result = sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])
    assert result == [1,4,5]

def test_sym_three_sets_number_elements():
    result = sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])
    assert len(result) == 3

def test_sym_sequence_3_ok():
    result = sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])
    assert result == [2, 3, 4, 6, 7]

def test_sym_sequence_3_number_elements():
    result = sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])
    assert len(result) == 5

def test_sym_sequence_4_ok():
    result = sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])
    assert result == [1, 2, 4, 5, 6, 7, 8, 9]

def test_sym_sequence_4_number_elements():
    result = sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])
    assert len(result) == 8
import pytest

def squre(n):
    return n**2

def cube(n):
    return n**3

# testing
def test_squre():
    assert squre(2) == 4, "test failed, squre should be 4"
    assert  squre(3) == 9, "test failed, squre should be 9"
def test_cube():
    assert cube(2) == 8, "test failed, cube should be 8"
    assert cube(3) == 27, "test failed, cube should be 27"
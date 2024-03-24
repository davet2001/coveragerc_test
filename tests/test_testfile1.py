import pytest

from testpackage.testfile1 import func1_mult

def test_func1_mult():
    res = func1_mult(5, 6)
    assert res == 30



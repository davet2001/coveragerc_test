import pytest

from testpackage.testfile2 import func2_add

def test_func2_add():
    res = func2_add(5, 6)
    assert res == 11

    

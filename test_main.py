import pytest

from main import *

def test_addition():
    assert addition(1,2) == 3
    assert addition(5,6) == 11

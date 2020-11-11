from series import __version__
from math_series.series import fibonacci, lucas, sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci():
    actual = fibonacci(n)
    expect = n
    assert actual == expected

def test_lucas():
    actual = lucas(n)
    expected = n
    assert actual == expected

def test_sum_series():
    actual = sum_series(n,a,g)
    expected = n 
    assert actual == expected
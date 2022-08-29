import pytest


# def inc(x):
#     return x + 1
#
# def test_answer():
#     assert inc(4) == 5
#
# def test_a():
#     a = 1
#     b = 3

@pytest.mark.parametrize("test_input,expected", [
    ("3+5",8),("2+5",7),("7+5",12)
], ids=["number1", "number2", 'number3'])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected
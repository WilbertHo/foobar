from solution import answer

from nose.tools import eq_

def test_answer():
    eq_(2, answer(["foo", "bar", "oof", "bar"]))
    eq_(5, answer(["x", "y", "xy", "yy", "", "yx"]))

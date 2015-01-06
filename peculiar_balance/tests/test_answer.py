import solution

from nose.tools import eq_

def test_answer():
    eq_(['L', 'R'], solution.answer(2))
    eq_(['L', '-', 'R'], solution.answer(8))
    eq_(['R'], solution.answer(1))
    eq_(['-', 'L', 'R', 'L', 'R'], solution.answer(60))

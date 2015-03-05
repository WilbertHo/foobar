from nose.tools import eq_
import squaresupplies


def test_answer():
    eq_(squaresupplies.answer(9), 1)
    eq_(squaresupplies.answer(160), 2)
    eq_(squaresupplies.answer(24), 3)

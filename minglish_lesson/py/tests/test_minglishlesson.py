from nose.tools import eq_
import minglishlesson


def test_answer():
    eq_(minglishlesson.answer(['c', 'cac', 'cb', 'bcc', 'ba']), 'cab')
    eq_(minglishlesson.answer(['y', 'z', 'xy']), 'yzx')
    eq_(minglishlesson.answer(['ba', 'ab', 'cb']), 'bac')

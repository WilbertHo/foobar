#!/usr/bin/env python

import solution

from nose.tools import eq_

def test_solution():
    eq_('03/19/19', solution.answer(19, 19, 3))
    eq_('Ambiguous', solution.answer(3, 30, 3))
    eq_('Ambiguous', solution.answer(1, 1, 3))
    eq_('01/01/01', solution.answer(1, 1, 1))
    eq_('11/13/99', solution.answer(99, 11, 13))
    eq_('Ambiguous', solution.answer(12, 31, 30))
    eq_('02/28/29', solution.answer(2, 28, 29))
    eq_('Ambiguous', solution.answer(2, 12, 12))


if __name__ == '__main__':
    main()

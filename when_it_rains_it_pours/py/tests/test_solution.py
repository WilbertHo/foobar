from nose.tools import eq_
import solution

def test_solution():
    eq_(solution.answer([1,4,2,5,1,2,3]), 5)
    eq_(solution.answer([1,2,3,2,1]), 0)
    eq_(solution.answer([2, 5, 1, 2, 3, 4, 7, 7, 6]), 10)
    eq_(solution.answer([2, 5, 1, 3, 1, 2, 1, 7, 7, 6]), 17)
    eq_(solution.answer([2, 7, 2, 7, 4, 7, 1, 7, 3, 7]), 18)
    eq_(solution.answer([6, 7, 7, 4, 3, 2, 1, 5, 2]), 10)
    eq_(solution.answer([2, 5, 1, 2, 3, 4, 7, 7, 6, 
                         2, 7, 1, 2, 3, 4, 5, 5, 4]), 26)
    #eq_(solution.answer([2,7,3,7,6,4,5,8,0,5,6,0,3,3,2]), 20)

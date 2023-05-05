# use pytest

from solver import solve, rebus_preprocessing

def test_rebus_solver():
    solutions = solve("КОЗА+КОЗА = СТАДО")
    solutions.sort()
    assert solutions == ["7693+7693 = 15386", "8653+8653 = 17306"]

def test_rebus_preprocessing():
    rpn_rebus, letters = rebus_preprocessing("КОЗА*2 = СТАДО")

    assert rpn_rebus == ["КОЗА","2",'*',"СТАДО",'-']
    assert letters == {'К','О','З','A','С','Т','Д'}

# use pytest

from solver import solve, rebus_preprocessing, naive_rebus_solver

def test_rebus_solver():
    solutions = solve("КОЗА+КОЗА = СТАДО")
    solutions.sort()
    assert solutions == ["7693+7693 = 15386", "8653+8653 = 17306"]

def test_rebus_preprocessing():
    rpn_rebus, letters = rebus_preprocessing("КОЗА*2 = СТАДО")

    assert rpn_rebus == ["КОЗА","2",'*',"СТАДО",'-']
    assert letters == {'К','О','З','A','С','Т','Д'}

def test_naive_rebus_solver():
    rpn_rebus, letters = rebus_preprocessing("КОЗА*2 = СТАДО")
    substitutions = naive_rebus_solver(rpn_rebus, letters)
    assert substitutions == [
        {'К':'8','О':'6','З':'5','A':'3','С':'1','Т':'7','Д':'0'},
        {'К':'7','О':'6','З':'9','A':'3','С':'1','Т':'5','Д':'8'}
    ]
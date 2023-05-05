# use pytest

from main import solve
from preprocessing import rebus_preprocessing
from solvers import naive_rebus_solver, ten_adic_rebus_solver
   

def test_rebus_preprocessing():
    rpn_rebus = rebus_preprocessing("КОЗА*2 = СТАДО")

    assert rpn_rebus == ["КОЗА","2",'*',"СТАДО",'-']

# def test_naive_rebus_solver():

#     solutions, substitutions = solve("КОЗА+КОЗА = СТАДО", naive_rebus_solver)

#     assert sorted(solutions) == ["7693+7693 = 15386", "8653+8653 = 17306"]

#     # для удобства проверки преобразуем список словарей 
#     # в отсортированный список кортеджей отсортированных пар 
#     substitutions_pairs = sorted([
#         tuple(sorted([tuple(item) for item in s.items()]))
#         for s in substitutions
#     ]) 
    
#     assert substitutions_pairs == [
#         (('А', '3'), ('Д', '0'), ('З', '5'), ('К', '8'), ('О', '6'), ('С', '1'), ('Т', '7')), 
#         (('А', '3'), ('Д', '8'), ('З', '9'), ('К', '7'), ('О', '6'), ('С', '1'), ('Т', '5'))
#     ]


def test_ten_adic_rebus_solver():

    solutions, substitutions = solve("КОЗА+КОЗА = СТАДО", ten_adic_rebus_solver)

    print(solutions, substitutions)

    assert sorted(solutions) == ["7693+7693 = 15386", "8653+8653 = 17306"]

    # для удобства проверки преобразуем список словарей 
    # в отсортированный список кортеджей отсортированных пар 
    substitutions_pairs = sorted([
        tuple(sorted([tuple(item) for item in s.items()]))
        for s in substitutions
    ]) 
    
    assert substitutions_pairs == [
        (('А', '3'), ('Д', '0'), ('З', '5'), ('К', '8'), ('О', '6'), ('С', '1'), ('Т', '7')), 
        (('А', '3'), ('Д', '8'), ('З', '9'), ('К', '7'), ('О', '6'), ('С', '1'), ('Т', '5'))
    ]
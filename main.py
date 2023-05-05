
from typing import Callable, Iterable, Iterator


from preprocessing import rebus_preprocessing
from solvers import naive_rebus_solver, ten_adic_rebus_solver, replace, parallel_solver


def solve(rebus: str, solver: Callable[[list[str]], list[dict[str,str]]]) -> list[str]:
    """ Главная функция решателя ребусов """

    rebus = rebus.upper()

    rpn_rebus = rebus_preprocessing(rebus)

    substitutions = solver(rpn_rebus)


    solutions = []

    for substitution in substitutions:
        solutions.append(replace(rebus, substitution))

    return solutions, substitutions


if __name__ == '__main__':

    rebus = 'трава+корова+доярка = молоко'

    print(rebus)

    import time
    start_time = time.time()

    solutions, substitutions = solve(rebus, parallel_solver)
    # solutions, substitutions = solve(rebus, naive_rebus_solver)

    print("--- %s seconds ---" % (time.time() - start_time))

    count = len(solutions)

    if count == 0:
        print('Solutions not found!')
    elif count == 1:
        print('Found one solution:')
    else:
        print(f'Found {count} solutions:')

    for solution in solutions:
        print('\t',solution)



from typing import Callable, Iterable, Iterator

from multiprocessing import Pool
from preprocessing import rebus_preprocessing
from solvers import naive_rebus_solver, ten_adic_rebus_solver, replace


# def parallel_solver(rpn_rebus: list[str], letters: set[str]) -> list[dict[int,str]]:
#     """ Распараллеленый наивный способ решения """
#     letters = parse_letters(rpn_rebus)

#     def single_permutation_test(args):

#         permutation, rpn_rebus = args

#         letters = parse_letters(rpn_rebus)
#         for i, s in enumerate(letters):
#             letters[s] = permutation[i]

#         table = str.maketrans(letters)

#         rpn_rebus_substitute = substitute(rpn_rebus, table) 
#         for word in rpn_rebus_substitute:
#             if word[0] == '0' and len(word)>1:
#                 return None
#         else:
#             if calc(rpn_rebus_substitute) == 0:
#                 return table
#             else:
#                 return None

#     tables = []

#     p = Pool(6)

#     def arg():
#         for p in permutations('0123456789', len(letters)):
#             yield (p, rpn_rebus)
    

#     tables = list(filter(lambda x: x, p.map(single_permutation_test, arg())))

#     return tables


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

    solutions, substitutions = solve(rebus, ten_adic_rebus_solver)
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


from itertools import permutations
import math
from multiprocessing import Pool


TRANSLATE = True # использовать ли str.translate и str.maketrans для замены
POOLS = 6 # сколько процессов будет запущено параллельно

# Решатели


def naive_rebus_solver(rpn_rebus: list[str]) -> list[dict[str,str]]:
    """ Наивный способ решения """

    substitutions = []

    letters = parse_letters(rpn_rebus)

    for permutation in permutations('0123456789', len(letters)):

        substitution = single_permutation_test((rpn_rebus, permutation, letters))
        if substitution:
            substitutions.append(substitution)

    return substitutions


def parallel_rebus_solver(rpn_rebus: list[str]) -> list[dict[str,str]]:
    """ Распараллеленый наивный способ решения """
    letters = parse_letters(rpn_rebus)

    p = Pool(POOLS)

    def arg():
        for permutation in permutations('0123456789', len(letters)):
            yield (rpn_rebus, permutation, letters)

    substitutions = list(filter (lambda x: x, p.map(single_permutation_test, arg())))

    return substitutions


def ten_adic_rebus_solver(rpn_rebus: list[str]) -> list[dict[str,str]]:
    """ Продвинутый способ решения """

    word_max_len = len(max(rpn_rebus, key=len))
    substitutions = []
    substitutions_part = [{}]

    for power in range(1, word_max_len+1):
        rpn_rebus_part = [word[-power:] for word in rpn_rebus]
        substitutions_part = ten_adic_rebus_solver_part(rpn_rebus_part, power, substitutions_part)

    for substitution in substitutions_part:

        if single_substitution_test(rpn_rebus, substitution):
            substitutions.append(substitution)

    return substitutions


def ten_adic_rebus_solver_part(rpn_rebus:list[str], power:int, old_substitutions:list[dict[str,str]]) -> list[dict[str,str]]:
    """ Одна итерация продвинутого способа решения 
        Принимает на вход урезанный ребус, степень и текущий словарь частичных решений. 
    """

    new_substitutions = []

    for old_substitution in old_substitutions:
        rpn_rebus_partly_substitute = replace_rpn_rebus(rpn_rebus, old_substitution)

        letters = parse_letters(rpn_rebus_partly_substitute)

        digits = set('0123456789') - set(old_substitution.values())

        for permutation in permutations(digits, len(letters)):

            delta_substitution = {}
            for i, s in enumerate(letters):
                delta_substitution[s] = permutation[i]

            if TRANSLATE:
                delta_substitution = str.maketrans(delta_substitution)

            new_substitution = delta_substitution | old_substitution

            rpn_rebus_substitute = replace_rpn_rebus(rpn_rebus_partly_substitute, new_substitution)

            if calc(rpn_rebus_substitute, power) == 0:

                new_substitutions.append(new_substitution)

    return new_substitutions



# общие функции


def single_permutation_test(args):

    rpn_rebus, permutation, letters = args

    substitution = {}

    for i, s in enumerate(letters):
        substitution[s] = permutation[i]

    if TRANSLATE:
        substitution = str.maketrans(substitution)

    if single_substitution_test(rpn_rebus, substitution):
        return substitution
    return None

        
def single_substitution_test(rpn_rebus, substitution) -> bool:
    """ проверка на то, что подстановка решает ребус"""
    rpn_rebus_substitute = replace_rpn_rebus(rpn_rebus, substitution) 

    for word in rpn_rebus_substitute:
        if word[0] == '0' and len(word)>1:
            return False
    else:
        if calc(rpn_rebus_substitute) == 0:
            return True
        else:
            return False
        

def parse_letters(rpn_rebus: list[str]) -> list[str]:
    """ Вычленение из RPN выражения списка незамененных букв """
    return [s for s in set(list(''.join(rpn_rebus))) if s.isalpha()]

def replace(string:str, substitution: dict[str,str]) -> str:
    """ Подстановка в строку словаря замены """

    if TRANSLATE:
        return string.translate(substitution)

    return ''.join([
        substitution.get(l,l)
        for l in string
    ])


def replace_rpn_rebus(rpn_rebus: list[str], substitution: dict[int,str]) -> list[str]:
    """ Подстановка в RPN выражение словаря замены """
    return [replace(token, substitution) for token in rpn_rebus]

def calc(rpn_expression: list[str], power: int = 0) -> int:
    """ Вычисление RPN выражения """

    if power:
        operators = {
            '+': lambda x, y: (x + y) % 10 ** power,
            '-': lambda x, y: (x - y) % 10 ** power,
            '*': lambda x, y: (x * y) % 10 ** power,
        }
    else:
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }

    stack:list[int] = []
    for term in rpn_expression:
        if term in operators:
            y, x = stack.pop(), stack.pop()
            stack.append(operators[term](x, y))
        else:
            stack.append(int(term))

    return stack[0]

from itertools import permutations
from typing import Iterable, Iterator

from multiprocessing import Pool

def rebus_preprocessing(rebus: str) -> tuple[list[str], set[str]]:
    """Валидация ребуса и вычисление его RPN"""

    operators = {
        '+': 1,
        '-': 1,
        '*': 2,
    }

    """ Шаг 1 """

    rebus_lowered = rebus.lower() # переводим в нижний регистр

    rebus_stripped = ''.join(rebus_lowered.split())  # убираем все пробельные символы

    rebus_splitted = rebus_stripped.split('=') # разбиваем на "до и после ="
     
    assert len(rebus_splitted) == 2, f'Выражение должно содержать один знак равенства, а не {len(rebus_splitted)}'
    assert rebus_splitted[0] and rebus_splitted[1], 'Некорректное выражение'

    rebus_ready = f'({rebus_splitted[0]})-({rebus_splitted[1]})'

    """ Шаг 2 """

    letters_set = set([s for s in rebus_ready if s.isalpha()])

    assert len(letters_set) <= 10, f'Число уникальных букв {len(letters_set)}>10: {letters_set}'

    symbols_set = set([s for s in rebus_ready if not s.isalpha() and not s.isdigit()])
    forbidden_symbols = symbols_set - set(operators.keys()) - {'(',')'}
    assert not forbidden_symbols, f'Есть неизвестные символы: {forbidden_symbols}'

    """ Шаг 3 """

    def splitter(formula_string: str) -> Iterator[str]:
        word = ''
        for s in formula_string:
            if s.isalpha() or s.isdigit():
                word += s
            elif word:
                yield word
                word = ''
            if s in operators or s in ['(',')']:
                yield s
        if word:
            yield word

    rebus_split = splitter(rebus_ready)

    """ Шаг 4 """

    def shunting_yard(parsed_formula: Iterable[str]) -> Iterator[str]:
        stack:list[str] = []
        for token in parsed_formula:
            if token in operators:
                while stack and stack[-1] != "(" and operators[token] <= operators[stack[-1]]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    rpn_rebus = list(shunting_yard(rebus_split))

    return rpn_rebus, letters_set



def calc(rpn_expression: Iterable[str], power: int = 0) -> int:
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



def substitute(rpn_rebus: list[str], table: dict[int,str]) -> list[str]:
    """ Подстановка в RPN выражение таблицы замены """
    return [word.translate(table) for word in rpn_rebus]



def parse_letters(rpn_rebus: list[str]) -> dict[str, str]:
    """ Вычленение из RPN выражения списка незамененных букв """
    letters_set = [s for s in set(list(''.join(rpn_rebus))) if s.isalpha()]
    return {s:s for s in letters_set}


def single_permutation_test(args):

    permutation, rpn_rebus = args

    letters = parse_letters(rpn_rebus)
    for i, s in enumerate(letters):
        letters[s] = permutation[i]

    table = str.maketrans(letters)

    rpn_rebus_substitute = substitute(rpn_rebus, table) 
    for word in rpn_rebus_substitute:
        if word[0] == '0' and len(word)>1:
            return None
    else:
        if calc(rpn_rebus_substitute) == 0:
            return table
        else:
            return None


def parallel_solver(rpn_rebus: list[str]) -> list[dict[int,str]]:
    """ Распараллеленый наивный способ решения """
    letters = parse_letters(rpn_rebus)

    tables = []

    p = Pool(6)

    def arg():
        for p in permutations('0123456789', len(letters)):
            yield (p, rpn_rebus)
    

    tables = list(filter(lambda x: x, p.map(single_permutation_test, arg())))

    return tables


def naive_solver(rpn_rebus: list[str]) -> list[dict[int,str]]:
    """ Наивный способ решения """
    letters = parse_letters(rpn_rebus)

    tables = []

    for permutation in permutations('0123456789', len(letters)):
        for i, s in enumerate(letters):
            letters[s] = permutation[i]

        table = str.maketrans(letters)

        rpn_rebus_substitute = substitute(rpn_rebus, table) 

        for word in rpn_rebus_substitute:
            if word[0] == '0' and len(word)>1:
                break
        else:
            if calc(rpn_rebus_substitute) == 0:
                tables.append(table)

    return tables


def ten_adic_solver(rpn_rebus: list[str]) -> list[dict[int,str]]:
    """ Продвинутый способ решения """

    word_max_len = len(max(rpn_rebus, key=len))
    tables = []
    table_parts:list[dict[int,str]] = [{}]

    for power in range(1, word_max_len+1):
        rpn_rebus_part = [word[-power:] for word in rpn_rebus]
        table_parts = ten_adic_solver_part(rpn_rebus_part, power, table_parts)

    for table in table_parts:
        rpn_expression = substitute(rpn_rebus, table)

        for word in rpn_expression:
            if word[0] == '0' and len(word)>1:
                break
        else:
            if calc(rpn_expression) == 0:
                tables.append(table)
    return tables

def ten_adic_solver_part(rpn_rebus:list[str], power:int, old_tables:list[dict[int,str]]) -> list[dict[int,str]]:
    """ Одна итерация продвинутого способа решения """

    new_tables = []

    for old_table in old_tables:
        rpn_rebus_partly_substitute = substitute(rpn_rebus, old_table)

        letters = parse_letters(rpn_rebus_partly_substitute)

        digits = set('0123456789') - set(old_table.values())

        for permutation in permutations(digits, len(letters)):
            for i, s in enumerate(letters):
                letters[s] = permutation[i]

            new_table = str.maketrans(letters) | old_table

            rpn_rebus_substitute = substitute(rpn_rebus_partly_substitute, new_table)

            if calc(rpn_rebus_substitute, power) == 0:
                new_tables.append(new_table)

    return new_tables


def solve(rebus: str) -> list[str]:
    """ Главная функция решателя ребусов """


    import time
    start_time = time.time()

    rebus = rebus.lower()

    rpn_rebus, letters_set = rebus_preprocessing(rebus)

    tables = ten_adic_solver(rpn_rebus)

    print("--- %s seconds ---" % (time.time() - start_time))

    solutions = []

    for table in tables:
        solutions.append(rebus.translate(table))

    return solutions


if __name__ == '__main__':

    rebus = 'трава+корова+доярка = молоко'
    print(rebus)
    solutions  = solve(rebus)

    count = len(solutions)

    if count == 0:
        print('Solutions not found!')
    elif count == 1:
        print('Found one solution:')
    else:
        print(f'Found {count} solutions:')

    for solution in solutions:
        print('\t',solution)


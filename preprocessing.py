from typing import Iterable, Iterator

def rebus_preprocessing(rebus: str) -> list[str]:
    """Валидация ребуса и вычисление его RPN"""

    operators = {
        '+': 1,
        '-': 1,
        '*': 2,
    }

    """ Шаг 1 """

    rebus_lowered = rebus.upper() # переводим в верхний регистр

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

    return rpn_rebus


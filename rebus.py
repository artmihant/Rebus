from itertools import permutations

OPERATORS = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y),
    '^': (3, lambda x, y: x ** y)
}


def parse(formula_string):
    word = ''
    for s in formula_string:
        if s.isalpha() or s.isdigit():
            word += s
        elif word:
            yield word
            word = ''
        if s in OPERATORS or s in "()=":
            yield s
    if word:
        yield word


def shunting_yard(parsed_formula):
    stack = []
    for token in parsed_formula:
        if token in OPERATORS:
            while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
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


def calc(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:
            y, x = stack.pop(), stack.pop()
            stack.append(OPERATORS[token][1](x, y))
        else:
            stack.append(token)
    return stack[0]


def solve(rebus):
    rebus = ''.join(rebus.split())  # убрать все пробелы

    rebus = rebus.split('=')

    assert len(rebus) == 2, 'Выражение должно содержать один знак равенства'
    assert rebus[0] and rebus[1], 'Некорректное выражение'

    polish_rebus = list(shunting_yard(parse('-'.join(rebus))))

    rebus = ' '.join(parse('='.join(rebus)))

    letters = {}

    for s in rebus:
        if s.isalpha():
            letters[s] = None

    assert len(letters) < 11

    answers = []

    for permutation in permutations(range(10), len(letters)):

        for i, s in enumerate(letters):
            letters[s] = str(permutation[i])

        table = ''.maketrans(letters)

        polish_rebus_permutate = [
            word if word in OPERATORS else
            int(word.translate(table))
            for word in polish_rebus]

        if calc(polish_rebus_permutate) == 0:
            answers.append(table)

    for ans in answers:
        print(rebus.translate(ans))

    print(list(letters.keys()))

    return rebus


if __name__ == '__main__':
    # print(list(shunting_yard(parse(formula))))

    print(solve('реши + если = силен'))
